import re

def parse_pdf_text(text):

    data = {}

    name = re.search(
        r"Name\s*:\s*(.+)",
        text
    )

    subject = re.search(
        r"Subject\s*:\s*(.+)",
        text
    )

    marks = re.search(
        r"Marks\s*:\s*(\d+)",
        text
    )

    if name:
        data["name"] = name.group(1).strip()

    if subject:
        data["subject"] = subject.group(1).strip()

    if marks:
        data["marks"] = marks.group(1).strip()

    return data