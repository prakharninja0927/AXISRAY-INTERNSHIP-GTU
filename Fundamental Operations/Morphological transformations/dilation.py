import cv2 as cv
import numpy as np
'''
It is just opposite of erosion. Here, a pixel element is '1' if atleast one pixel under the kernel is '1'.
it increases the white region in the image or size of foreground object increases. 
 
'''

# read an image
img = cv.resize(src= cv.imread('../Resources/Photos/name.png'), dsize=(700, 400), interpolation=cv.INTER_CUBIC)
cv.imshow('Original Image',img)

# performing dilation
kernel=np.ones((5,5),np.uint8)
dilated_img = cv.dilate(src=img,kernel=kernel, iterations=1)
cv.imshow('Dilated Image',dilated_img)

cv.waitKey(0)