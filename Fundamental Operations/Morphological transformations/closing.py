import cv2 as cv
import numpy as np

'''
Closing is reverse of Opening, Dilation followed by Erosion. 
It is useful in closing small holes inside the foreground objects, or small black points on the object.

'''
# read an image
img = cv.resize(src= cv.imread('../Resources/Photos/name1.png'), dsize=(700, 400), interpolation=cv.INTER_CUBIC)
cv.imshow('Original Image',img)

# performing Closing
kernel=np.ones((5,5),np.uint8)
closing = cv.morphologyEx(src = img,kernel = kernel,op = cv.MORPH_CLOSE)
cv.imshow('Opening image',closing)

cv.waitKey(0)