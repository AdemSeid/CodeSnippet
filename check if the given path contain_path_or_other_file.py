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
        # Print the path and name of the folder if it doesn't contain subfolders
        print("Folder Path:", path)
        print("Folder Name:", os.path.basename(path))


# Replace 'path_to_fldr' with the actual path to your folder
path_to_fldr = r'C:\Users\Adam\Documents\PR\Image_dataset\Folder5'

if os.path.exists(path_to_fldr) and os.path.isdir(path_to_fldr):
    list_folders(path_to_fldr)
else:
    print("The specified path does not exist or is not a directory.")


var = "Hel"
print(f'hi{var}')


'''
import os

# Define the folder name stored in the 'folder_name' variable
folder_name = "animal"

# Create the full folder name with "result" appended
full_folder_name = folder_name + " result"

# Initialize a counter to append to the folder name if needed
counter = 1
new_folder_name = full_folder_name

# Check if the folder already exists
while os.path.exists(new_folder_name):
    # If it does, add a number inside parentheses and check again
    counter += 1
    new_folder_name = f"{full_folder_name}({counter})"

# Create the final folder
os.makedirs(new_folder_name)

# Your code to save the file in the folder
# Replace this line with your code to save the file
# For example, you can use shutil.copy() or any other method to save the file.
# Here's an example of how you can copy a file to the created folder:
import shutil
file_to_save = "your_file.txt"  # Replace with the actual file you want to save
shutil.copy(file_to_save, os.path.join(new_folder_name, os.path.basename(file_to_save)))

# Now, the file will be saved in the folder with the appropriate name (e.g., "animal result(1)").


'''




