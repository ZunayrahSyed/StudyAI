from upload_pdf import upload_pdf
import pdfplumber
def extract_text(path):
    with pdfplumber.open(path) as pdf:
        text=''
        for i in pdf.pages:
            text+=i.extract_text()
    print(len(text))


path=input("Input path to the file: ")
Proceed=upload_pdf(path)
if Proceed:
    extract_text(path)
