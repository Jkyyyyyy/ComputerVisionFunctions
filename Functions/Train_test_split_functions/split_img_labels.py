import os
from pathlib import Path

directory = "/home/yolov7/yolov7-main/Building_Labelled_img/2_3_images_labelled"

pic_folder = os.path.join(directory, 'images')
txt_folder = os.path.join(directory, 'labels')

os.makedirs(pic_folder, exist_ok=True)
os.makedirs(txt_folder, exist_ok=True)

for filename in os.listdir(directory):
    file_path = os.path.join(directory, filename)

    if filename.endswith('.jpg'):
        new_file_path = os.path.join(pic_folder, filename)
        os.rename(file_path, new_file_path)

    elif filename.endswith('.JPG'):
        new_file_path = os.path.join(pic_folder, filename)
        os.rename(file_path, new_file_path)

    elif filename.endswith('.PNG'):
        new_file_path = os.path.join(pic_folder, filename)
        os.rename(file_path, new_file_path)

    elif filename.endswith('.png'):
        new_file_path = os.path.join(pic_folder, filename)
        os.rename(file_path, new_file_path)

    elif filename.endswith('.txt'):
        new_file_path = os.path.join(txt_folder, filename)
        os.rename(file_path, new_file_path)