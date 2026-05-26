<<<<<<< HEAD
import faiss
import numpy as np 

def chunk_text(text,chunk_size=500,overlap=100):
    chunks=[]
    start=0
    while start<len(text):
        end=start+chunk_size
        chunk=text[start:end]
        chunks.append(chunk)
        start+=chunk_size-overlap
    
    return chunks

from sentence_transformers import SentenceTransformer
model=SentenceTransformer("all-MiniLM-L6-v2")
def create_embedding(chunks):
    embeddings=model.encode(chunks)
    return embeddings

def create_faiss_index(embeddings):
    embeddings=np.array(embeddings)
    dimension=embeddings.shape[1]
    index=faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index 

def embed_query(query):
    return model.encode([query])

def search(index,query_embedding,k=3):
    dist,ind=index.search(query_embedding,k)
    return dist,ind
=======
import faiss
import numpy as np 

def chunk_text(text,chunk_size=500,overlap=100):
    chunks=[]
    start=0
    while start<len(text):
        end=start+chunk_size
        chunk=text[start:end]
        chunks.append(chunk)
        start+=chunk_size-overlap
    
    return chunks

from sentence_transformers import SentenceTransformer
model=SentenceTransformer("all-MiniLM-L6-v2")
def create_embedding(chunks):
    embeddings=model.encode(chunks)
    return embeddings

def create_faiss_index(embeddings):
    embeddings=np.array(embeddings)
    dimension=embeddings.shape[1]
    index=faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    return index 

def embed_query(query):
    return model.encode([query])

def search(index,query_embedding,k=3):
    dist,ind=index.search(query_embedding,k)
    return dist,ind
>>>>>>> c55ef92f5cbf4d7ebb45c635610cb3537a88c623
