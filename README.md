# PDF-Chatbot
 PDF Chatbot

A simple AI-powered chatbot that lets you upload a PDF and ask questions about its content.
Instead of reading the whole document, you get direct answers with page references.

✨ What It Does
Upload any PDF (research, report, book, etc.)
Ask questions in natural language
Get AI-generated answers based only on the document
See page numbers for verification
 How It Works

The project uses RAG (Retrieval-Augmented Generation).

PDF is loaded and text is extracted
Text is split into small chunks
Each chunk is converted into embeddings
Embeddings are stored in a vector database
User question is also converted into embedding
Most relevant chunks are retrieved
LLM generates answer based only on those chunks
 Why RAG?

Instead of sending the whole PDF to the model:

Only relevant parts are used
Faster responses
Lower cost
Higher accuracy
 Project Structure
main.py        → API layer (routes & requests)
pdf_utils.py   → PDF reading & text extraction
rag.py         → chunking, embeddings, retrieval logic
llm.py         → AI model interaction
config.py      → environment configuration
logger.py      → logging system
📡 API Endpoints
GET  /health
→ Check if server is running
POST /upload
→ Upload PDF file
→ Returns document ID
POST /ask/{doc_id}
→ Ask question about the PDF
→ Returns:
   - Answer
   - Source chunks
   - Page numbers
 Configuration

All settings are stored in a .env file:

Model name
Chunk size
Overlap size
Retrieval settings
API keys

No sensitive data is hardcoded.

 Deployment

Project supports Docker and Docker Compose.

docker-compose up --build

Features:

Persistent storage for PDFs
Persistent vector index
One-command deployment
 Testing

Includes basic tests for:

PDF parsing
Chunking logic
Retrieval system
API endpoints
Edge cases (invalid file, missing document)
 Summary

PDF Chatbot is a simple RAG-based system that allows you to query documents intelligently.
It retrieves only relevant parts of the PDF and uses them to generate accurate answers with source references.