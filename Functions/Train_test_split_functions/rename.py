import os

def rename(source_dir, strg):
    for filename in os.listdir(source_dir):
        new_name = strg + filename
        file_path = os.path.join(source_dir, filename)
        new_path = os.path.join(source_dir, new_name)
        os.rename(file_path,new_path)

rename('/home/yolov7/yolov7-main/Building_Labelled_img/2_3_images_labelled/images','C')
rename('/home/yolov7/yolov7-main/Building_Labelled_img/2_3_images_labelled/labels','C')