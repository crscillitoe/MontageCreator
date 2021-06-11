import glob
from moviepy.editor import *

# Grab a list of all files in the clips directory
video_files = glob.glob("../Recordings/*")

# Grab all clips in the Recordings folder named "sion_ornn"
# And play them in sequential order, in black and white,
# slowed down to 75% speed.
edited = (
    concatenate_videoclips(
        [VideoFileClip(v) for v in sorted(video_files) if v[14:23] == "sion_ornn"]
    )
    .fx(vfx.blackwhite)
    .fx(vfx.speedx, factor=0.75)
)

# Apply music and write file
edited.set_audio(
    afx.audio_loop(AudioFileClip("music.wav"), duration=edited.duration)
).write_videofile("sion_ornn.mp4")
