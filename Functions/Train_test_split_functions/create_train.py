import os
import shutil
from pathlib import Path
import random

directory = '/home/yolov7/yolov7-main/training_v4'
img_dir = '/home/yolov7/yolov7-main/images_v4/images'
label_dir = '/home/yolov7/yolov7-main/images_v4/labels'

new_img_dir = '/home/yolov7/yolov7-main/training_v4/images'
new_label_dir = '/home/yolov7/yolov7-main/training_v4/labels'

val_file = os.path.join(directory, 'val.txt')
train_file = os.path.join(directory, 'train.txt')

img_train_folder = os.path.join(new_img_dir, 'train')
img_val_folder = os.path.join(new_img_dir, 'val')
label_train_folder = os.path.join(new_label_dir, 'train')
label_val_folder = os.path.join(new_label_dir, 'val')

os.makedirs(img_train_folder, exist_ok=True)
os.makedirs(img_val_folder, exist_ok=True)
os.makedirs(label_train_folder, exist_ok=True)
os.makedirs(label_val_folder, exist_ok=True)

selected_files = random.sample(os.listdir(img_dir), int(len(os.listdir(img_dir)) * 0.2))

with open(val_file, 'w') as v_f, open(train_file, 'w') as t_f:
    
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

        if selected_files.__contains__(filename):
            new_file_path = os.path.join(img_val_folder, filename)
            if img_file_path != new_file_path:
                shutil.move(img_file_path, new_file_path)
            v_f.write(f'{new_file_path}\n')

            new_file_path = os.path.join(label_val_folder, matching_files)
            if label_file_path != new_file_path:
                shutil.move(label_file_path, new_file_path)

            
        else:
            new_file_path = os.path.join(img_train_folder, filename)
            if img_file_path != new_file_path:
                shutil.move(img_file_path, new_file_path)
            t_f.write(f'{new_file_path}\n')

            new_file_path = os.path.join(label_train_folder, matching_files)
            if label_file_path != new_file_path:
                shutil.move(label_file_path, new_file_path)



