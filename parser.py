def parse_ocr(texts):

    result = {}

    for i in range(len(texts)):

        if texts[i] == "Name":
            result["name"] = texts[i+1]

        if texts[i] == "Subject":
            result["subject"] = texts[i+1]

        if texts[i] == "Marks":
            result["marks"] = texts[i+1]

    return result