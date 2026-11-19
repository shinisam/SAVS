from signature_verifier import verify_signature


result = verify_signature(

    "uploads/forged.pdf",

    "uploads/official_result.pdf.sig",

    "keys/public.pem"

)

print(result)