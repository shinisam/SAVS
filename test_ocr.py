import easyocr

print("Loading OCR Engine...")

reader = easyocr.Reader(['en'])

print("OCR Engine Loaded")

result = reader.readtext("sample.png")

print("\nDetected Text:\n")

for item in result:
    print(item[1])