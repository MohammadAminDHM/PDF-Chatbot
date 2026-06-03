import faiss
import numpy as np 
import nltk
import os 
from sentence_transformers import SentenceTransformer
from config import CHUNK_SIZE, OVERLAP, TOP_K



def chunk_text(pages_data,chunk_size=CHUNK_SIZE,overlap=OVERLAP):
    chunks=[]

    for page in pages_data:
        text = page["text"]
        page_num = page["page"]

        sentences=nltk.sent_tokenize(text)

        current_chunk=""

        for sentence in sentences:
            if len(current_chunk) + len(sentence) <= chunk_size:
                current_chunk += " " + sentence
            else:
                if current_chunk.strip():
                    chunks.append({
                        "text": current_chunk.strip(),
                        "page": page_num
                    })
                words = current_chunk.split()
                overlap_text = " ".join(words[-overlap:]) if len(words) > overlap else current_chunk
                current_chunk = overlap_text + " " + sentence
        
        if current_chunk.strip():
            chunks.append({
                "text": current_chunk.strip(),
                "page": page_num
            })
    
    return chunks
                

model=SentenceTransformer("all-MiniLM-L6-v2")

def create_embedding(chunks):
    texts=[chunk["text"] for chunk in chunks]
    embeddings=model.encode(texts)
    faiss.normalize_L2(embeddings)
    return embeddings

def create_faiss_index(embeddings):
    embeddings=np.array(embeddings)
    dimension=embeddings.shape[1]
    index=faiss.IndexFlatIP(dimension)
    index.add(embeddings)
    return index 

def save_index(index,path):
    faiss.write_index(index,path)

def load_index(path):
    return faiss.read_index(path)

def embed_query(query):
    embedding=model.encode([query])
    faiss.normalize_L2(embedding)
    return embedding


def search(index, query_embedding, k=TOP_K):
    scores, indices = index.search(query_embedding, k)
    return scores, indices
