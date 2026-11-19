import cv2
import qrcode
import json


def generate_qr(payload):

    qr = qrcode.make(
        json.dumps(payload)
    )

    path = "static/qr_token.png"

    qr.save(path)

    return path


def read_qr(image_path):

    detector = cv2.QRCodeDetector()

    img = cv2.imread(image_path)

    data, bbox, _ = detector.detectAndDecode(img)

    if not data:
        return None

    return json.loads(data)


def verify_qr(
        qr_data,
        parsed_data):

    if qr_data is None:
        return False

    return (
        str(qr_data["marks"])
        ==
        str(parsed_data["marks"])
    )