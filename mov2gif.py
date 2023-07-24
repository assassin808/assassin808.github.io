from moviepy.editor import VideoFileClip

videoClip = VideoFileClip("Untitled.mov")
videoClip.write_gif("tankwar.gif", program='ffmpeg', fps=videoClip.fps/12)
