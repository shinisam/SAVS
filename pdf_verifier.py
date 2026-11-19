import fitz


def get_pdf_metadata(pdf_path):

    pdf = fitz.open(pdf_path)

    metadata = pdf.metadata

    pdf.close()

    return metadata


def extract_pdf_text(pdf_path):

    pdf = fitz.open(pdf_path)

    text = ""

    for page in pdf:
        text += page.get_text()

    pdf.close()

    return text