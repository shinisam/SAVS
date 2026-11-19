from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas


def generate_report(
        parsed_data,
        report):

    pdf_path = "static/forensic_report.pdf"

    c = canvas.Canvas(
        pdf_path,
        pagesize=letter
    )

    c.setFont("Helvetica-Bold", 18)

    c.drawString(
        50,
        750,
        "SAVS FORENSIC REPORT"
    )

    c.setFont("Helvetica", 12)

    c.drawString(
        50,
        700,
        f"Name: {parsed_data['name']}"
    )

    c.drawString(
        50,
        680,
        f"Subject: {parsed_data['subject']}"
    )

    c.drawString(
        50,
        660,
        f"Submitted Mark: {parsed_data['marks']}"
    )

    c.drawString(
        50,
        640,
        f"Official Mark: {report['official']}"
    )

    c.drawString(
        50,
        620,
        f"Status: {report['status']}"
    )

    c.drawString(
        50,
        600,
        f"Risk Score: {report['score']}%"
    )

    c.drawString(
        50,
        560,
        "Evidence Summary"
    )

    c.drawString(
        70,
        540,
        "- OCR Extraction Completed"
    )

    c.drawString(
        70,
        520,
        "- Database Verification Completed"
    )

    c.drawString(
        70,
        500,
        "- ELA Forensic Analysis Completed"
    )
    
    c.drawImage(
    "static/uploads/ela_output.png",
    50,
    100,
    width=250,
    height=150
    )
    c.drawImage(
    "static/qr_token.png",
    400,
    600,
    width=100,
    height=100
    )
    
    c.save()

    return pdf_path