from PIL import Image
from PIL import ImageChops


def perform_ela(image_path):

    original = Image.open(image_path)

    if original.mode == "RGBA":
        original = original.convert("RGB")

    temp_file = "temp.jpg"

    original.save(
        temp_file,
        "JPEG",
        quality=90
    )

    compressed = Image.open(temp_file)

    ela_image = ImageChops.difference(
        original,
        compressed
    )

    extrema = ela_image.getextrema()

    max_diff = max(
        ex[1] for ex in extrema
    )

    if max_diff == 0:
        max_diff = 1

    scale = 255.0 / max_diff

    ela_image = ela_image.point(
        lambda p: p * scale
    )

    ela_path = "static/uploads/ela_output.png"

    ela_image.save(ela_path)

    return ela_path