from moviepy.video.io.VideoFileClip import VideoFileClip


video = VideoFileClip("data/1A-Cam001.mp4")

frame_rate = video.fps
print(f"Video Frame Rate: {frame_rate} FPS")

start_time = 6  * 60 + 0
end_time = 6 * 60 + 30

video_clip = video.subclip(start_time, end_time)
video_clip.write_videofile("data/video4.mp4", codec="libx264", fps=video.fps)
video.close()
