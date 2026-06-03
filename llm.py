from openai import OpenAI
from config import OPENAI_API_KEY, MODEL_NAME, BASE_URL
import os


client = OpenAI(
    api_key=OPENAI_API_KEY,
    base_url=BASE_URL
)

def generate_answer(question, chunks):
    context = ""
    for chunk in chunks:
        context += f"[Page {chunk['page']}]: {chunk['text']}\n\n"
    
    prompt = f"""Answer the question based only on the context below.
If the answer is not in the context, say "I could not find enough information in the document."

Context:
{context}

Question: {question}

Answer:"""

    response = client.chat.completions.create(
        model=MODEL_NAME,
        messages=[{"role": "user", "content": prompt}],
        max_tokens=500,
        temperature=0.3
    )
    
    return response.choices[0].message.content