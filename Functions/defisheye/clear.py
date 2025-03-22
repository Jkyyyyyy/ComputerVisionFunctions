import os
import shutil

# Specify the folder to delete all files and folders from
folder_path = "/home/testing/testing"

# Delete all files and folders in the folder
for filename in os.listdir(folder_path):
    file_path = os.path.join(folder_path, filename)
    if os.path.isfile(file_path):
        os.remove(file_path)
    elif os.path.isdir(file_path):
        shutil.rmtree(file_path)