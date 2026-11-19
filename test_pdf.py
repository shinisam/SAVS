from pdf_verifier import *

print("\n===== PDF METADATA =====\n")

meta = get_pdf_metadata(
    "forged.pdf"
)

print(meta)

print("\n===== PDF CONTENT =====\n")

text = extract_pdf_text(
    "genuine.pdf"
)

print(text)