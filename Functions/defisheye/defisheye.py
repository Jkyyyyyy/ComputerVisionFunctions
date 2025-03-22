import cv2
import numpy as np
import math
import os
import matplotlib.pyplot as plt
from pathlib import Path
from PIL import Image, ImageDraw

source_dir = '/home/testing/dataimg'        ## Change to Source Location
save_dir = '/home/testing/testing'          ## Change to Save Location
width, height = 1300, 2600                  ## Change to required output size
boundary = 1000                             ## Change to required output boundary

# Perspective Matrix h                      ## Change according to camera
                # BL,BR,TL,TR  
src = np.array([[-384,980],[1435,1570],[1225,333],[1800,444]])
dst = np.array([[boundary, height+boundary],[width+boundary,height+boundary],[boundary,boundary],[width+boundary,boundary]])
H, m = cv2.findHomography(src, dst)

# Camera matrix, distortion coefficients    ## Change according to camera
#camera_matrix = np.array([[1.8388e+03, 0.0, 9.5021e+02],
#                          [0.0, 1.8388e+03, 5.4563e+02],
#                          [0.0, 0.0, 1.0]])

camera_matrix = np.array([[1.5985e+03, 0.0000e+00, 9.5021e+02],
                          [0.0000e+00, 1.5985e+03, 5.4563e+02],
                          [0.0000e+00, 0.0000e+00, 1.0000e+00]])

distortion_coeffs = np.array([-0.3811, 0.1573, 0.0026, 0.0002, -0.0474])

CONST_IMG_WIDTH = 1920                      ## IMG PIXEL WIDTH
CONST_IMG_HEIGHT = 1080                      ## IMG PIXEL HEIGHT

##### Input: (float) X pixel coordinate of original img
#            (float) Y pixel coordinate of original img
#### Output: (float) X pixel coordinate of 2D map
#            (float) Y pixel coordinate of 2D map
#            (array) XY coordinate
def transform(x_coordinate, y_coordinate):
    # Transform to 2D coordinate
    input_coordinate = np.array([[x_coordinate, y_coordinate]], dtype='float32')
    input_coordinate = np.array([input_coordinate])
    transformed_coordinate = cv2.perspectiveTransform(input_coordinate, H)

    return float(transformed_coordinate[0][0][0]), float(transformed_coordinate[0][0][1]) ,transformed_coordinate


##### Input: (float) X pixel coordinate of point 1 on map
#            (float) Y pixel coordinate of point 1 on map
#            (float) X pixel coordinate of point 2 on map
#            (float) Y pixel coordinate of point 2 on map
#### Output: (float) Distance between point 1 & 2
def get_distance(x1,y1,x2,y2):
    return float(math.sqrt((x1-x2)**2+(y1-y2)**2))


##### Input: (Array) Array of Lines in txt file
#### Output: (float) X pixel coordinate of original img
#            (float) Y pixel coordinate of original img
def get_person_location(box_array):
    ## Case of Person
    if (get_box_type(box_array) == 0):
        # Case 1: Can locate feet
        if ((get_box_Y(box_array) + get_box_height(box_array)/2) < 0.99):
            return float(get_box_X(box_array) * CONST_IMG_WIDTH), float((get_box_Y(box_array)+ get_box_height(box_array)/2) * CONST_IMG_HEIGHT)

        # Case 2: Cannot locate feet
        else:
            return None

    ## Case of Baby
    else:
        return None


##### Other Functions
def get_box_type(box_array):
    return int(box_array[0])

def get_box_X(box_array):
    return float(box_array[1])

def get_box_Y(box_array):
    return float(box_array[2])

def get_box_width(box_array):
    return float(box_array[3])

def get_box_height(box_array):
    return float(box_array[4])


##### MAIN
# Read labelimg txt files
# Output a txt file to store the map of all image   
files = [f for f in os.listdir(source_dir) if f.endswith('.txt')]

for file in files:
    file_path = os.path.join(source_dir, file)
    save_path = os.path.join(save_dir, file)
    filename = os.path.splitext(file)[0]

    img_read = f"{source_dir}/{filename}.png"
    img_save = f"{save_dir}/{filename}.png"

    # Undistort the fisheye effect of the image
    img = cv2.imread(img_read)

    h, w = img.shape[:2]
    newcameramtx, roi = cv2.getOptimalNewCameraMatrix(camera_matrix, distortion_coeffs, (w, h), 1, (w, h))
    undistorted = cv2.undistort(img, camera_matrix, distortion_coeffs, None, newcameramtx)
    x, y, w, h = roi
#    undistorted = undistorted[y:y+h, x:x+w]

    # Transforming real picture to 2d plane
    output_img = cv2.warpPerspective(undistorted, H, (width+boundary*2, height+boundary*2))

    # Make location txt file & Red dot presentations 
    image = Image.fromarray(cv2.cvtColor(output_img, cv2.COLOR_BGR2RGB))
    draw = ImageDraw.Draw(image)
    radius = 10

    with open(file_path, 'r') as r_f, open(save_path, 'w') as s_f:
        for line in r_f.readlines():
            words = line.split(' ')

            # Change to 2D coordinate and Save in another file
            if (get_person_location(words) != None):
                p_x, p_y = get_person_location(words)
                undistorted_location = cv2.undistortPoints(np.array([[p_x, p_y]], dtype=np.float32), camera_matrix, distortion_coeffs, None, newcameramtx)
                p_x = undistorted_location[0][0][0]
                p_y = undistorted_location[0][0][1]

                x, y, xy = transform(p_x , p_y)
                s_f.writelines([str(x),' ', str(y),'\n'])
            
            # Make graphical presentation
                draw.ellipse((x - radius, y - radius, x + radius, y + radius), outline=(255, 0, 0), width=4)

    image.save(img_save)