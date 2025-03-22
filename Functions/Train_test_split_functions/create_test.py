import os
import shutil
from pathlib import Path
import random

directory = '/home/yolov7/yolov7-main/testing_v4'
img_dir = '/home/yolov7/yolov7-main/images_v4/images'
label_dir = '/home/yolov7/yolov7-main/images_v4/labels'

new_img_dir = '/home/yolov7/yolov7-main/testing_v4/images'
new_label_dir = '/home/yolov7/yolov7-main/testing_v4/labels'

train_file = os.path.join(directory, 'train.txt')

img_train_folder = os.path.join(new_img_dir, 'train')
label_train_folder = os.path.join(new_label_dir, 'train')

os.makedirs(img_train_folder, exist_ok=True)
os.makedirs(label_train_folder, exist_ok=True)

with open(train_file, 'w') as t_f:
    
    for filename in os.listdir(img_dir):
        img_file_path = os.path.join(img_dir, filename)

        Name = os.path.splitext(filename)[0]
        for f in os.listdir(label_dir):
            if Name == os.path.splitext(f)[0]:
                matching_files = f
                break
            else:
                matching_files = '0'

        if matching_files == '0':
            continue
        
        label_file_path = os.path.join(label_dir, matching_files)

        new_file_path = os.path.join(img_train_folder, filename)
        if img_file_path != new_file_path:
            shutil.move(img_file_path, new_file_path)
        t_f.write(f'{new_file_path}\n')

        new_file_path = os.path.join(label_train_folder, matching_files)
        if label_file_path != new_file_path:
            shutil.move(label_file_path, new_file_path)



