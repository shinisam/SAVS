from pdf_verifier import *
from pdf_parser import *
from verifier import verify_student

text = extract_pdf_text(
    "forged.pdf"
)

parsed = parse_pdf_text(text)

print("Parsed Data")
print(parsed)

print("\nVerification Result")

result = verify_student(
    parsed["name"],
    parsed["subject"],
    parsed["marks"]
)

print(result)