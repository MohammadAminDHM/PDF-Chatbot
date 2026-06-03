from pypdf import PdfReader 

def load_pdf(path):
    reader=PdfReader(path)
    pages_data=[]

    for page_num , page in enumerate(reader.pages):
        text=page.extract_text()
        if not text or not text.strip():
            continue

        pages_data.append({
            "text":text,
            "page":page_num+1
        })

    return pages_data


    