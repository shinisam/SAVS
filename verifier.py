import json

def verify_student(name, subject, uploaded_mark):
    name = name.strip()
    subject = subject.strip()
    uploaded_mark = str(uploaded_mark).strip()
    with open("database.json") as file:
        data = json.load(file)

    if name not in data:

        return {
            "status": "Student Not Found",
            "score": 50
        }

    official_mark = data[name][subject]

    if int(uploaded_mark) == official_mark:

        return {
            "status": "AUTHENTIC",
            "score": 5,
            "official": official_mark
        }

    return {
        "status": "TAMPERING SUSPECTED",
        "score": 95,
        "official": official_mark
    }