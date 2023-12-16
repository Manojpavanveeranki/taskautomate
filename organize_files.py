import os
import shutil

def organize_files(source_folder, destination_folder):
    # Ensure the destination folder exists
    os.makedirs(destination_folder, exist_ok=True)

    # Iterate through files in the source folder
    for filename in os.listdir(source_folder):
        source_path = os.path.join(source_folder, filename)

        # Skip directories
        if os.path.isdir(source_path):
            continue

        # Get the file extension
        _, extension = os.path.splitext(filename)
        extension = extension.lower()

        # Create a subfolder for the file type if it doesn't exist
        type_folder = os.path.join(destination_folder, extension[1:])
        os.makedirs(type_folder, exist_ok=True)

        # Move the file to the corresponding subfolder
        destination_path = os.path.join(type_folder, filename)
        shutil.move(source_path, destination_path)
        print(f"Moved: {filename} to {type_folder}")

if __name__ == "__main__":
    # Specify the source and destination folders
    source_folder = "/path/to/source/folder"
    destination_folder = "/path/to/destination/folder"

    # Organize files
    organize_files(source_folder, destination_folder)
