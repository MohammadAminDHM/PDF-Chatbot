<<<<<<< HEAD
from fastapi import FastAPI
from pydantic import BaseModel
from pdf_utils import load_pdf
from rag import chunk_text, create_embedding, create_faiss_index, embed_query, search

# ساخت app
app = FastAPI()

# لود کردن PDF هنگام شروع برنامه
pdf_path = r"C:\Users\NoteBook\Desktop\pdf-chatbot\data\Eye.pdf"
text = load_pdf(pdf_path)
chunks = chunk_text(text)
embeddings = create_embedding(chunks)
index = create_faiss_index(embeddings)

# تعریف ساختار درخواست
class Question(BaseModel):
    question: str

# endpoint اصلی
@app.post("/ask")
def ask(body: Question):
    query_embedding = embed_query(body.question)
    dist, ind = search(index, query_embedding)
    
    results = [chunks[i] for i in ind[0]]
=======
from fastapi import FastAPI
from pydantic import BaseModel
from pdf_utils import load_pdf
from rag import chunk_text, create_embedding, create_faiss_index, embed_query, search

# ساخت app
app = FastAPI()

# لود کردن PDF هنگام شروع برنامه
pdf_path = r"C:\Users\NoteBook\Desktop\pdf-chatbot\data\Eye.pdf"
text = load_pdf(pdf_path)
chunks = chunk_text(text)
embeddings = create_embedding(chunks)
index = create_faiss_index(embeddings)

# تعریف ساختار درخواست
class Question(BaseModel):
    question: str

# endpoint اصلی
@app.post("/ask")
def ask(body: Question):
    query_embedding = embed_query(body.question)
    dist, ind = search(index, query_embedding)
    
    results = [chunks[i] for i in ind[0]]
>>>>>>> c55ef92f5cbf4d7ebb45c635610cb3537a88c623
    return {"answer": results}