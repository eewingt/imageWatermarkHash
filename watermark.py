## apply watermark for 1 image

import cv2
"""
#provide a dialog to choose directory.
from tkinter import Tk     # from tkinter import Tk for Python 3.x
from tkinter.filedialog import askopenfilename


Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filedir = askopenfilename() # show an "Open" dialog box and return the path to the selected file
print(filedir)
"""

# open an image using opencv
imgOriginal = cv2.imread('watermarkingimage\Capture.png')
img = imgOriginal
#img = cv2.resize(imgOriginal, (640, 304))  - resizing an image will determine a default size for all images.

cv2.imshow('Boehringer Ingelheim', img)

# get image height and width
height, width, channels = img.shape

# add watermark
blue = (255, 0, 0)
position = (width - 300, height - 25)
font = cv2.FONT_HERSHEY_COMPLEX_SMALL
cv2.putText(img, "Boehringer Ingelheim",
    position, font, 0.7, blue, 1)

cv2.imshow('Boehringer Ingelheim', img)

# save image using opencv
cv2.imwrite('watermarkingimage\capture2.jpg', img)

# key controller
cv2.waitKey(0)
cv2.destroyAllWindows()