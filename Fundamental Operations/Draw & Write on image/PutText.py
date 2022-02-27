import os

import cv2 as cv
import numpy as np
import os
import glob

# Create blank image using numpy
blank_img = np.zeros((600,600,3), dtype=np.uint8)

cv.putText(img=blank_img,text='OpenCV', org=(10,500), fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=4, color=(255,255,255),thickness=2
           ,lineType=cv.LINE_AA)
cv.imshow('BLank Text',blank_img)

# Print name of file image on image
folder_dir = "../Resources/Faces/"
extensions = ['png', 'jpg', 'gif', 'jpeg']
images = []
[images.extend(glob.glob(folder_dir + '*' + e)) for e in extensions]

for img in images:
    image_name = os.path.basename(img).split(".")[0]
    img = cv.imread(img)
    cv.putText(img=img, text=f'{image_name}',
               org=(30, 100), fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=3, color=(0, 255, 0))
    cv.imshow(f'{image_name}', img)
cv.waitKey(0)