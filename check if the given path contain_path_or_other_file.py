
import os

def list_folders(path):
    has_subfolders = False  # Initialize a flag to check if the folder has subfolders
    for root, dirs, files in os.walk(path):
        for folder in dirs:
            folder_path = os.path.join(root, folder)
            print("Folder Path:", folder_path)
            print("Folder Name:", folder)
            has_subfolders = True  # Set the flag to True if subfolders are found
    
    if not has_subfolders:
        print("Folder Path:", path)
        print("Folder Name:", os.path.basename(path))


# Replace 'path_to_fldr' with the actual path to your folder
path_to_fldr = r'C:\Users\Adam\Documents\PR\Image_dataset\Folder5'

if os.path.exists(path_to_fldr) and os.path.isdir(path_to_fldr):
    list_folders(path_to_fldr)
else:
    print("The specified path does not exist or is not a directory.")

