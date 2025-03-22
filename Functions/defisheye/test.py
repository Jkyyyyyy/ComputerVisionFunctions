import cv2
import numpy as np
import math
import os
from pathlib import Path

show_img_dir = '/home/testing/dataimg/1A-Cam001_177_01.png'
source_dir = '/home/testing/dataimg'
save_dir = '/home/testing/testing/test_trail'
count = 1

while os.path.isdir(save_dir):
    if save_dir != '/home/testing/testing/test_trail':
        save_dir = save_dir[:-1]
    save_dir = save_dir + str(count)
    count += 1

os.makedirs(save_dir)

#                          Vertical bend
#camera_matrix = np.array([[1.8388e+03, 0.0, 9.5021e+02],

#                              Horizontal bend
#                          [0.0, 1.8388e+03, 5.4563e+02],

#
#                          [0.0, 0.0, 1.0]])

#distortion_coeffs = np.array([-0.3811, 0.1573, 0.0026, 0.0002, -0.0474])

# Camera matrix, distortion coefficients    ## Change according to camera
camera_matrix = np.array([[1.5985e+03, 0.0000e+00, 9.5021e+02],
                          [0.0000e+00, 1.5985e+03, 5.4563e+02],
                          [0.0000e+00, 0.0000e+00, 1.0000e+00]])
distortion_coeffs = np.array([-0.3811, 0.1573, 0.0026, 0.0002, -0.0474])

img = cv2.imread(show_img_dir)

files = [f for f in os.listdir(source_dir) if f.endswith('.txt')]

for file in files:
    file_path = os.path.join(source_dir, file)
    save_path = os.path.join(save_dir, file)
    filename = os.path.splitext(file)[0]

    img_read = f"{source_dir}/{filename}.png"
    img_save = f"{save_dir}/{filename}.png"

    img = cv2.imread(img_read)

    h, w = img.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, distortion_coeffs, (w, h), 1, (w, h))
    undistorted = cv2.undistort(img, camera_matrix, distortion_coeffs, None, newcameramtx)
    x, y, w, h = roi
#    undistorted = undistorted[y:y+h, x:x+w]

    cv2.imwrite(img_save, undistorted)
