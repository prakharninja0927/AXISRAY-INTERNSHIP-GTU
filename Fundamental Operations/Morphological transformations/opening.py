import cv2 as cv
import numpy as np

'''
Opening is just another name of erosion followed by dilation. 
It is useful in removing noise, as we explained above. Here we use the function,

'''
# read an image
img = cv.resize(src= cv.imread('../Resources/Photos/name1.png'), dsize=(700, 400), interpolation=cv.INTER_CUBIC)
img = cv.resize(img, (400,250), cv.INTER_AREA)
cv.imshow('Original Image',img)

# performing opening
kernel=np.ones((5,5),np.uint8)
opening = cv.morphologyEx(src = img,kernel = kernel,op = cv.MORPH_OPEN)
closing = cv.morphologyEx(src = img,kernel = kernel,op = cv.MORPH_CLOSE)
cv.imshow('Opening image',opening)
cv.imshow('Closing image',closing)

cv.waitKey(0)