from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
from cryptography.hazmat.primitives import serialization


def verify_signature(
        pdf_path,
        signature_path,
        public_key_path):

    try:

        with open(
            public_key_path,
            "rb"
        ) as key_file:

            public_key = serialization.load_pem_public_key(
                key_file.read()
            )

        with open(
            pdf_path,
            "rb"
        ) as pdf_file:

            pdf_data = pdf_file.read()

        with open(
            signature_path,
            "rb"
        ) as sig_file:

            signature = sig_file.read()

        public_key.verify(

            signature,

            pdf_data,

            padding.PSS(

                mgf=padding.MGF1(
                    hashes.SHA256()
                ),

                salt_length=
                padding.PSS.MAX_LENGTH

            ),

            hashes.SHA256()

        )

        return True

    except Exception:

        return False