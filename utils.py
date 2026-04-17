import PyPDF2
import pytesseract
from PIL import Image

def extract_pdf(file):
    reader = PyPDF2.PdfReader(file)
    text = ""
    for page in reader.pages:
        if page.extract_text():
            text += page.extract_text()
    return text

def extract_image(file_path):
    img = Image.open(file_path)
    return pytesseract.image_to_string(img)

def detect_risks(text):
    keywords = ["diabetes", "cancer", "infection", "hypertension"]
    return [k for k in keywords if k in text.lower()]
