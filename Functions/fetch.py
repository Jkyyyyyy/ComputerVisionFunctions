import cv2
import os

def get_frames(vid, store_loc):
    cap = cv2.VideoCapture(vid)
    i = 0
    frame_skip = 60  # The skip rate of fetching frames
    frame_count = 0
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        if i > frame_skip - 1:
            frame_count += 1
            frame = cv2.resize(frame, (1920, 1080))
            cv2.imwrite(store_loc + str(frame_count)+'.jpg', frame)
            i = 0
            continue
        i += 1

    cap.release()
    cv2.destroyAllWindows()


def list_mp4_files(folder_path):
    mp4_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            if file.endswith('.MP4'):
                mp4_files.append(os.path.join(root, file))
    return mp4_files


# You should change to where you keep the MP4 files
folder_path = "/home/Building_labelled/Example_folder_path"

mp4_file_paths = list_mp4_files(folder_path)

count = 1
for path in mp4_file_paths:

    # You should change to store dir (store_loc), images will be stored in new created folders in the dir
    # E.g. Autocreate folder 1 in store_loc, Video 1 will be stored in 1
    #      Autocreate folder 2 in store_loc, Video 2 will be stored in 2
    store_loc = "/home/Building_labelled/Example_store_loc/" + str(count) +"/"
    if not os.path.exists(store_loc):
        os.makedirs(store_loc)

    get_frames(path, store_loc)
    count += 1