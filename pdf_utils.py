<<<<<<< HEAD
from pypdf import PdfReader 

def load_pdf(path):
    reader=PdfReader(path)
    text=""
    for page in reader.pages:
        text+=page.extract_text()
    return text
=======
from pypdf import PdfReader 

def load_pdf(path):
    reader=PdfReader(path)
    text=""
    for page in reader.pages:
        text+=page.extract_text()
    return text
>>>>>>> c55ef92f5cbf4d7ebb45c635610cb3537a88c623
    