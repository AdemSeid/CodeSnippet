import os
from PIL import Image

def read_images():
    folder_path = 'C:\\Users\\Adam\\Documents\\PR\\Star\\API\\image'  # Specify your folder path here
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif']  # Add more extensions if needed
    image_files = [f for f in os.listdir(folder_path) if os.path.isfile(os.path.join(folder_path, f)) and f.lower().endswith(tuple(image_extensions))]
    image_paths = []

    for file_name in image_files:
        image_path = os.path.join(folder_path, file_name)
        image_paths.append(image_path)

    # Start a task with resizing optio

    return image_paths

image_paths = read_images()

print("directory of all images")
print(image_paths)
