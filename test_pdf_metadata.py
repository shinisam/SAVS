from pdf_verifier import get_pdf_metadata

meta = get_pdf_metadata(
    "forged.pdf"
)

print(meta)