from fastapi import APIRouter, UploadFile, File, HTTPException
from PyPDF2 import PdfReader
import os

router = APIRouter()

@router.post("/")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    try:
        file_path = f"{file.filename}"
        with open(file_path, "wb") as temp_file:
            temp_file.write(await file.read())

        pdf_text = extract_text_from_pdf(file_path)
        return {"filename": file.filename, "text": pdf_text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred while processing the file: {e}")

def extract_text_from_pdf(file_path):
    try:
        reader = PdfReader(file_path)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        cleaned_text = " ".join(text.split())
        return cleaned_text

    except Exception as e:
        print(f"Error extracting text from PDF: {e}")
        raise Exception(f"Failed to extract text from PDF: {e}")