from PIL import Image
import os


def resize_image(image_path, width, height):

    img = Image.open(image_path)

    resized = img.resize((width, height))

    base, ext = os.path.splitext(image_path)

    new_path = f"{base}_resized{ext}"

    resized.save(new_path)

    return new_path