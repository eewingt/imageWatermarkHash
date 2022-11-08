import numpy as np
import moviepy.editor as mp
import glob

#declare array variables
outfile = []
file_name = []
list_rows = []

#set the watermarking logo image
wm = 'logo.png'

# to perform watermarking on all videos in video folder. *caution will overwrite existing videos.
for filename in glob.glob('video/*.*'):
    file_name = filename
    video = mp.VideoFileClip(file_name)
    logo = (mp.ImageClip(wm).set_duration(video.duration))
    fnl = mp.CompositeVideoClip([video, logo])
    outfile = file_name
    fnl.subclip(0).write_videofile(outfile)
    np.savetxt("videowatermark.csv", outfile, delimiter=",", fmt='% s')
