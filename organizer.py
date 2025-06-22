import os
import shutil

downloads_path = r"C:\Users\USER\file_organizer_project\downloads_folder"

file_types = {
    'images': ['.jpg', '.jpeg', '.png'],
    'Documents': ['.pdf', '.docx', '.txt'],
    'Video': ['.mp4', '.mov'],
    'Audio': ['.mp3', '.wav'],
    'Others': []
}

source_folder = r'C:\Users\USER\file_organizer_project\downloads_folder'

for filename in os.listdir(downloads_path):
    file_path = os.path.join(downloads_path, filename)

    # Skip folders, only work with files
    if os.path.isfile(file_path):
        _, ext = os.path.splitext(filename)

        for folder_name, extensions in file_types.items():
            if ext.lower() in extensions:
                target_folder = os.path.join(downloads_path, f"{folder_name}_folder")

                # Create the folder if it doesn't exist
                if not os.path.exists(target_folder):
                    os.makedirs(target_folder)

                # Move the file
                shutil.move(file_path, os.path.join(target_folder, filename))
                print(f"Moved {filename} to {folder_name}_folder")
                break
