import pdfplumber
def upload_pdf(path):
    try:
        with pdfplumber.open(path):
            return True

    except Exception as e:
        print("Error:",e)
        return False