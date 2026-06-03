from dotenv import load_dotenv
import os 
load_dotenv()
OPENAI_API_KEY=os.getenv("OPENAI_API_KEY")
MODEL_NAME=os.getenv("MODEL_NAME")
CHUNK_SIZE = int(os.getenv("CHUNK_SIZE", 500))
OVERLAP = int(os.getenv("OVERLAP", 100))
TOP_K = int(os.getenv("TOP_K", 3))
BASE_URL = "https://api.avalai.ir/v1"