import os
import numpy as np
import cv2
import pi_heif

def convert_heic_folder_to_png(input_folder, output_folder="convertedPng"):
    # Create the output folder if it doesn't exist
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # Iterate over all files in the input folder
    for filename in os.listdir(input_folder):
        if filename.lower().endswith(".heic"):
            # Full path to the HEIC image
            heic_image_path = os.path.join(input_folder, filename)
            
            # Open the HEIC image file
            heif_file = pi_heif.open_heif(heic_image_path, convert_hdr_to_8bit=False, bgr_mode=True)
            # Convert HEIC to numpy array
            np_array = np.asarray(heif_file)
            # Extract the base name of the image (without extension)
            image_name = os.path.splitext(filename)[0]
            # Construct the full path for the output PNG image
            output_path = os.path.join(output_folder, f"{image_name}.png")
            # Save the image as PNG
            cv2.imwrite(output_path, np_array)
            print(f"Converted {heic_image_path} to {output_path}")

# Example usage
input_folder = "input"  # Replace with your input folder containing HEIC images
convert_heic_folder_to_png(input_folder)
