# write a python function to read jpg image and convert it to bytes then write it to a file


import base64
import sys
from PIL import Image
import io


def jpeg_to_base64(image_path, output_file):
    """Read a JPEG image and convert it to base64

    :param image_path: path to the image file
    :param output_file: path to the output file

    How to use:
    python3 img_to_base64.py image.jpg output.txt
    """
    # Open the JPEG image
    with Image.open(image_path) as image:
        # Convert the image to bytes
        buffered = io.BytesIO()
        image.save(buffered, format="JPEG")
        img_byte = buffered.getvalue()

        # Encode the bytes to base64
        img_base64 = base64.b64encode(img_byte)

        # Write the base64 string to a text file
        with open(output_file, "w") as file:
            file.write(img_base64.decode())


if __name__ == "__main__":
    image_file = sys.argv[1]
    output_file = sys.argv[2]
    jpeg_to_base64(image_file, output_file)
