
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

def grayscale_image(image_path):

    img = Image.open(image_path)

    grayscale = img.convert("L")

    base_dir = os.path.dirname(image_path)
    base_name, ext = os.path.splitext(os.path.basename(image_path))

    new_filename = f"{base_name}_gray{ext}"

    new_path = os.path.join(base_dir, new_filename)

    grayscale.save(new_path)

    return new_filename

def sepia_image(image_path):

    img = Image.open(image_path)

    sepia_matrix = (
        0.393, 0.769, 0.189, 0,
        0.349, 0.686, 0.168, 0,
        0.272, 0.534, 0.131, 0
    )

    sepia_img = img.convert('RGB', matrix=sepia_matrix)
    base_dir = os.path.dirname(image_path)
    base_name, ext = os.path.splitext(os.path.basename(image_path))

    new_filename = f"{base_name}_sepia{ext}"

    new_path = os.path.join(base_dir, new_filename)
    sepia_img.save(new_path)

    return new_filename

