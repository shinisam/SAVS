
from importlib.resources import path

from os import path

from flask import Flask
from flask import render_template
from flask import request
from ocr_engine import extract_text
from parser import parse_ocr
from verifier import verify_student
from risk_engine import calculate_risk
from forensic import perform_ela
from report_generator import generate_report
from pdf_verifier import *
from pdf_parser import *
import uuid
from datetime import datetime
from case_manager import save_case, load_cases,get_case
from qr_verifier import *
from signature_verifier import verify_signature

import os

app = Flask(__name__)

UPLOAD_FOLDER = "static/uploads"

os.makedirs(
    UPLOAD_FOLDER,
    exist_ok=True
)

@app.route("/")
def home():

    return render_template(
        "index.html",
         report=None,
        parsed_data=None,
        metadata=None,
        evidence_type=None,
        case_id=None,
        timestamp=None,
        risk_score=None,
        pdf_file=None,
        ela_image=None,
        image_name=None,
        signature_valid=None
    )
def get_file_type(filename):

    filename = filename.lower()

    if filename.endswith(
        (".png", ".jpg", ".jpeg")
    ):
        return "image"

    if filename.endswith(".pdf"):
        return "pdf"

    return "unknown"
@app.route("/cases")
def view_cases():

    cases = load_cases()

    return render_template(
        "cases.html",

        cases=cases
    )
@app.route("/case/<case_id>")
def case_details(case_id):

    case = get_case(case_id)

    return render_template(
        "case_details.html",

        case=case
    )
@app.route(
    "/upload",
    methods=["POST"]
)
def upload():

    file = request.files["image"]

    path = os.path.join(
        UPLOAD_FOLDER,
        file.filename
    )

    file.save(path)

    file_type = get_file_type(
        file.filename
    )

    if file_type == "image":

        return process_image(
            path,
            file.filename
        )

    elif file_type == "pdf":

        return process_pdf(
            path,
            file.filename
        )

    return "Unsupported File"
def process_image(
        path,
        filename):
    case_id = "AEGIS-" + str(uuid.uuid4())[:8].upper()
    ela_path = perform_ela(path)

    ocr_text = extract_text(path)

    parsed = parse_ocr(
        ocr_text
    )

    report = verify_student(
        parsed["name"],
        parsed["subject"],
        parsed["marks"]
    )
    case_id = "AEGIS-" + str(uuid.uuid4())[:8].upper()
    timestamp = datetime.now().strftime(
        "%d-%m-%Y %H:%M:%S"
    
    )
    
    
    mismatch = (
        report["status"] ==
        "TAMPERING SUSPECTED"
    )
    risk_score = calculate_risk(
        mismatch=mismatch,
        forensic=True,
        metadata=False
)   
    save_case({

    "case_id": case_id,

    "evidence_type": "Screenshot",

    "name": parsed["name"],

    "subject": parsed["subject"],

    "submitted_mark": parsed["marks"],

    "official_mark": report.get(
        "official",
        "N/A"
    ),

    "status": report["status"],

    "risk": risk_score,

    "timestamp": timestamp

    })
    return render_template(
        "index.html",
        evidence_type="Screenshot",
        image_name=filename,
        parsed_data=parsed,
        report=report,
        ela_image=True,
        risk_score=risk_score,
        case_id=case_id,
        timestamp=timestamp,
        pdf_file="forensic_report.pdf"
    )
def process_pdf(
        path,
        filename):
    case_id = "AEGIS-" + str(uuid.uuid4())[:8].upper()
    metadata = get_pdf_metadata(path)

    text = extract_pdf_text(path)
    qr_data = {
    
        "student":"22CS101",
    
        "name":"Arun Kumar",
    
        "subject":"Maths",  
    
        "marks":"75"
        }
    parsed = parse_pdf_text(text)
    qr_valid = verify_qr(
    qr_data,
    parsed
    )


    signature_file = path + ".sig"

    if os.path.exists(signature_file):

        signature_valid = verify_signature(

        path,

        signature_file,

        "keys/public.pem"

    )
        print("PDF PATH:", path)
        print("SIGNATURE FILE:", signature_file)
        print("SIGNATURE VALID:", signature_valid)
    else:

        signature_valid = None
        signature_valid = verify_signature(

        path,

        path + ".sig",

        "keys/public.pem"

    )
    report = verify_student(
        parsed["name"],
        parsed["subject"],
        parsed["marks"]
    )
    case_id = "AEGIS-" + str(uuid.uuid4())[:8].upper()
    timestamp = datetime.now().strftime(
         "%d-%m-%Y %H:%M:%S"
    )
   
    mismatch = (
        report["status"]
        == "TAMPERING SUSPECTED"
    )

    risk_score = calculate_risk(
        mismatch=mismatch,
        forensic=False,
        metadata=False,
        qr_valid=qr_valid,
        signature_valid=signature_valid
    )

    save_case({

        "case_id": case_id,

        "evidence_type":"PDF",

        "name": parsed["name"],

        "subject": parsed["subject"],

        "submitted_mark": parsed["marks"],

        "official_mark": report.get(
        "official",
        "N/A"
    ),

        "qr_data": qr_data,

        "qr_valid": qr_valid,
    
        "signature_valid": signature_valid,

        "status": report["status"],

        "risk": risk_score,

        "timestamp": timestamp

    })
    return render_template(
        "index.html",

        evidence_type="PDF",

        metadata=metadata,

        parsed_data=parsed,

        report=report,

        risk_score=risk_score,
        case_id=case_id,
        timestamp=timestamp,
        signature_valid=signature_valid,
        pdf_file="forensic_report.pdf"
    )

if __name__ == "__main__":

    app.run(debug=True)
