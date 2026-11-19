import json

def save_case(case_data):

    try:

        with open(
            "cases.json",
            "r"
        ) as file:

            cases = json.load(file)

    except:

        cases = []

    cases.append(case_data)

    with open(
        "cases.json",
        "w"
    ) as file:

        json.dump(
            cases,
            file,
            indent=4
        )
def load_cases():

    try:

        with open(
            "cases.json",
            "r"
        ) as file:

            return json.load(file)

    except:

        return []
def get_case(case_id):

    cases = load_cases()

    for case in cases:

        if case["case_id"] == case_id:

            return case

    return None