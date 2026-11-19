# test_qr_read.py

from qr_verifier import read_qr

data = read_qr(
    "static/qr_token.png"
)

print(data)