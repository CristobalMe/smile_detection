import argparse
from PIL import Image
import os

def convert_ppm_to_jpg(input_ppm_image, output_directory):
    # Open the .ppm image
    img = Image.open(input_ppm_image)
    # Create the output .jpg image name
    output_jpg_image_name = os.path.join(output_directory, os.path.basename(input_ppm_image).replace('.ppm', '.jpg'))
    # Save the image as .jpg
    img.save(output_jpg_image_name)
    print(f"Converted {input_ppm_image} to {output_jpg_image_name}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Convert PPM image to JPG.')
    parser.add_argument('input_ppm_image', type=str, help='Path to the input PPM image')
    parser.add_argument('output_directory', type=str, help='Directory to save the output JPG image')

    args = parser.parse_args()
    convert_ppm_to_jpg(args.input_ppm_image, args.output_directory)