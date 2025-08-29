import fitz  
from docx import Document
import os


def extract_text():
    upload_dir = "uploads"
    if len(os.listdir(upload_dir))== 0:
        return "No file found in the directory"
    for file in os.listdir(upload_dir):
        file_path = os.path.join(upload_dir, file)  
        root, ext = os.path.splitext(file)

        if ext.lower() == ".pdf":
            extracted_text = ""
            pdf = fitz.open(file_path)  
            for page in pdf:
                extracted_text += page.get_text()
            pdf.close()
            return extracted_text

        elif ext.lower() == ".docx":
            docx = Document(file_path)  
            extracted_text = []
            for paragraph in docx.paragraphs:
                extracted_text.append(paragraph.text)
            return "\n".join(extracted_text)  # better formatting

        else:
            return "Oopsie!! Text can't be extracted"
