
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

def rotate_image(image_path, angle):
    img = Image.open(image_path)

    rotated = img.rotate(angle, expand=True)

    base_dir = os.path.dirname(image_path)
    base_name, ext = os.path.splitext(os.path.basename(image_path))

    new_filename = f"{base_name}_rot{angle}{ext}"
    new_path = os.path.join(base_dir, new_filename)

    rotated.save(new_path)

    return new_path