
from PIL import Image
import os


def resize_image(image_path, width, height):

    img = Image.open(image_path)

    resized = img.resize((width, height))

    base, ext = os.path.splitext(image_path)

    filename = f"{os.path.basename(base)}_resized{ext}"

    new_path = os.path.join(
        os.path.dirname(image_path),
        filename
    )

    resized.save(new_path)

    return filename