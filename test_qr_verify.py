# test_qr_verify.py

from qr_verifier import *

qr_data = {

    "student":"22CS101",

    "name":"Arun Kumar",

    "subject":"Maths",

    "marks":"75"
}

parsed_data = {

    "name":"Arun Kumar",

    "subject":"Maths",

    "marks":"95"
}

result = verify_qr(
    qr_data,
    parsed_data
)

print(result)