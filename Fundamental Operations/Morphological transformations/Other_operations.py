import cv2 as cv
import numpy as np

# read an image
img = cv.resize(src= cv.imread('../Resources/Photos/name1.png'), dsize=(500, 350), interpolation=cv.INTER_CUBIC)
cv.imshow('Original Image',img)


# 1. Morphological Gradient:It is the difference between dilation and erosion of an image.
# The result will look like the outline of the object.
kernel=np.ones((5,5),np.uint8)
gradient = cv.morphologyEx(src = img,kernel = kernel,op = cv.MORPH_GRADIENT)
cv.imshow('Morphological Gradient',gradient)

# 2. Morphological Top Hat :It is the difference between input
# image and Opening of the image. Below example is done for a 5x5 kernel.
kernel=np.ones((5,5),np.uint8)
morph_topHat = cv.morphologyEx(src = img,kernel = kernel,op = cv.MORPH_TOPHAT)
cv.imshow('Morphological Top Hat',morph_topHat)

# 3. Morphological Black Hat:It is the difference between the closing of the input image
# and input image.
kernel=np.ones((29,29),np.uint8)
morph_blackHat = cv.morphologyEx(src = img,kernel = kernel,op = cv.MORPH_BLACKHAT)
cv.imshow('Morphological Black Hat',morph_blackHat)


cv.waitKey(0)