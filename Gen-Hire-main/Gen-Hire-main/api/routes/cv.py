from fastapi import APIRouter
from agents.cv_parser import parse_all_cvs
import fitz
import os

router = APIRouter()

CV_FOLDER = "data/CVs1"

def extract_text_from_pdf(pdf_path):
    text = ""
    try:
        with fitz.open(pdf_path) as doc:
            for page in doc:
                text += page.get_text()
        return text
    except Exception as e:
        return f"Error reading {pdf_path}: {str(e)}"

@router.get("/all")
def get_all_cvs():
    cvs_data = []
    for file_name in os.listdir(CV_FOLDER):
        if file_name.endswith(".pdf"):
            pdf_path = os.path.join(CV_FOLDER, file_name)
            content = extract_text_from_pdf(pdf_path)
            cvs_data.append({
                "file_name": file_name,
                "content": content
            })
    return cvs_data