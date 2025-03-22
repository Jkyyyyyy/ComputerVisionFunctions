import os
import shutil
from pathlib import Path
import random

os.remove('/home/yolov7/yolov7-main/training_v4/train.txt')
os.remove('/home/yolov7/yolov7-main/training_v4/val.txt')
os.remove('/home/yolov7/yolov7-main/training_v4/train.cache')
os.remove('/home/yolov7/yolov7-main/training_v4/val.cache')

def move_images(source_dir, target_dir):
  for filename in os.listdir(source_dir):
    if filename.lower().endswith(('.jpg', '.JPG', '.png','.txt')):
      source_path = os.path.join(source_dir, filename)
      target_path = os.path.join(target_dir, filename)
      shutil.move(source_path, target_path)

move_images('/home/yolov7/yolov7-main/training_v4/images/train','/home/yolov7/yolov7-main/training_v4/images')
move_images('/home/yolov7/yolov7-main/training_v4/images/val','/home/yolov7/yolov7-main/training_v4/images')
move_images('/home/yolov7/yolov7-main/training_v4/labels/train','/home/yolov7/yolov7-main/training_v4/labels')
move_images('/home/yolov7/yolov7-main/training_v4/labels/val','/home/yolov7/yolov7-main/training_v4/labels')

#os.remove('/home/yolov7/yolov7-main/training_v4/images/train')
#os.remove('/home/yolov7/yolov7-main/training_v4/images/val')
#os.remove('/home/yolov7/yolov7-main/training_v4/labels/train')
#os.remove('/home/yolov7/yolov7-main/training_v4/labels/val')

move_images("/home/yolov7/yolov7-main/training_v4/images", "/home/yolov7/yolov7-main/images_v4/images")
move_images("/home/yolov7/yolov7-main/training_v4/labels", "/home/yolov7/yolov7-main/images_v4/labels")