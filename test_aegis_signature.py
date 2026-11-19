# test_aegis_signature.py

from signature_verifier import verify_signature

result = verify_signature(

    "static/uploads/official_result.pdf",

    "static/uploads/official_result.pdf.sig",

    "keys/public.pem"

)

print(result)