from PyPDF2 import PdfReader

def ExtractTextFromPDF(filPath):
    reader = PdfReader(filePath)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text
