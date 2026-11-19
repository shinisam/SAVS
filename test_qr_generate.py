# test_qr_generate.py

from qr_verifier import generate_qr

payload = {
    "student":"22CS101",
    "name":"Arun Kumar",
    "subject":"Maths",
    "marks":"75"
}

generate_qr(payload)

print("QR Created Successfully")