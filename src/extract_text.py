import fitz
import pytesseract
from pdf2image import convert_from_path

def extract_text(pdf_path):

    doc = fitz.open(pdf_path)
    text = ""

    for page in doc:
        text += page.get_text()

    # OCR fallback if text is very small
    if len(text.strip()) < 50:
        images = convert_from_path(pdf_path)

        for img in images:
            text += pytesseract.image_to_string(img)

    return text