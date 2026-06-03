from fastapi import FastAPI, UploadFile, File, HTTPException
from pydantic import BaseModel
from pdf_utils import load_pdf
from rag import chunk_text, create_embedding, create_faiss_index, embed_query, search, save_index
from llm import generate_answer
from logger import get_logger
import uuid
import os

app = FastAPI()
documents = {}
log=get_logger("main")

class Question(BaseModel):
    question: str

@app.get("/health")
def health():
    log.info("health check")
    return {"status": "ok"}

@app.post("/upload")
async def upload_pdf(file: UploadFile = File(...)):
    log.info(f"start uploading...{file.filename}")
    if not file.filename.endswith(".pdf"):
        log.warning(f"this is not a pdf file{file.filename}")
        raise HTTPException(status_code=400, detail="just PDF file")
    
    doc_id = str(uuid.uuid4())
    os.makedirs("data", exist_ok=True)
    os.makedirs("indexes", exist_ok=True)
    
    file_path = f"data/{doc_id}.pdf"
    with open(file_path, "wb") as f:
        f.write(await file.read())
    
    pages_data = load_pdf(file_path)
    if not pages_data:
        log.error(f"PDF is empty{file.filename}")
    chunks = chunk_text(pages_data)
    embeddings = create_embedding(chunks)
    index = create_faiss_index(embeddings)
    save_index(index, f"indexes/{doc_id}.index")
    
    documents[doc_id] = {
        "filename": file.filename,
        "chunks": chunks,
        "index": index
    }

    log.info(f" complet : {file.filename} — {len(chunks)} chunk — doc_id: {doc_id}")

    return {"doc_id": doc_id, "filename": file.filename, "chunks": len(chunks)}

@app.post("/ask/{doc_id}")
def ask(doc_id: str, body: Question):
    if doc_id not in documents:
        log.warning(f"please insert doc id{doc_id}")
        raise HTTPException(status_code=404, detail="Document not found")
    
    log.info(f"Question: '{body.question}' — doc_id: {doc_id}")


    doc = documents[doc_id]
    query_embedding = embed_query(body.question)
    scores, ind = search(doc["index"], query_embedding)
    
    # chunk های مرتبط
    relevant_chunks = []
    for i, score in zip(ind[0], scores[0]):
        relevant_chunks.append({
            "text": doc["chunks"][i]["text"],
            "page": doc["chunks"][i]["page"],
            "score": round(float(score), 3)
        })
        
    log.info(f"Besdt Score: {relevant_chunks[0]['score']} — Page {relevant_chunks[0]['page']}")

    # جواب کامل از LLM
    answer = generate_answer(body.question, relevant_chunks)
    
    log.info(f"the answer for doc_id is: {doc_id}")

    return {
        "doc_id": doc_id,
        "answer": answer,
        "sources": relevant_chunks
    }