import cv2
import torch
from collections import deque
import numpy as np


names = ["person", "person_moving", "person_hand_swinging", "person_hit_baby", "person_push_baby", "baby_falling"]
colors = {
    "person": (255, 0, 0),
    "person_moving": (0, 255, 0),
    "person_hand_swinging": (0, 0, 255),
    "person_hit_baby": (255, 255, 0),
    "person_push_baby": (255, 0, 255),
    "baby_falling": (0, 255, 255)
}


# model pt file
# model = torch.hub.load('WongKinYiu/yolov7', 'custom', 'your model path')
model = torch.hub.load('WongKinYiu/yolov7', 'custom', '/home/kid_abuse_data/best.pt')
# video path
video_path = '/home/kid_abuse_data/original_data/5A/5A-Cam001.mp4'


cap = cv2.VideoCapture(video_path)
frame_queue = deque(maxlen=10)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = cap.get(cv2.CAP_PROP_FPS)
out = cv2.VideoWriter('output_video.mp4', cv2.VideoWriter_fourcc(*'mp4v'), fps, (width, height))

while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break
    frame_resized = cv2.resize(frame, (width, height))
    frame_queue.append(frame_resized)
    if len(frame_queue) == 10:
        frame_stack = frame_queue[0].copy()
        for i in range(1, len(frame_queue)):
            frame_stack = cv2.addWeighted(frame_stack, 0.5, frame_queue[i], 0.5, 0)
        results = model(frame_stack)
        labels, coords = results.xyxyn[0][:, -1], results.xyxyn[0][:, :-1]
        for i in range(len(labels)):
            row = coords[i]
            if row[4] >= 0.5:
                x1, y1, x2, y2 = int(row[0] * width), int(row[1] * height), int(row[2] * width), int(row[3] * height)
                label = names[int(labels[i])]
                color = colors.get(label, (255, 255, 255))
                cv2.rectangle(frame_stack, (x1, y1), (x2, y2), color, 2)
                cv2.putText(frame_stack, f'{label}: {row[4]:.2f}', (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)
        out.write(frame_stack)
        cv2.imshow('Concatenated YOLO Detection', frame_stack)
        frame_queue.popleft()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
out.release()
cv2.destroyAllWindows()
