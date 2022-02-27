import cv2
import cv2 as cv
import numpy as np
# read images
img1 = cv.resize(src=cv.imread('../Resources/Photos/round.png'),dsize=(600,600),interpolation=cv.INTER_CUBIC)
img2 = cv.resize(src=cv.imread('../Resources/Photos/star.png'),dsize=(600,600),interpolation=cv.INTER_CUBIC)
moon = cv.resize(src=cv.imread('../Resources/Photos/moon.jpeg'),dsize=(600,600),interpolation=cv.INTER_CUBIC)

cv.imshow('img1',img1)
cv.imshow('img2',img2)

# subtract images
'''This directly adds up image pixels in the two images. '''
simple_add = cv.subtract(src1=img2,src2=img1)
cv.imshow('Subtract',simple_add)
cv.imshow('Moon Subtracter',cv.subtract(src1=img1,src2=moon))
cv.imshow('Moon Subtracter2',cv.subtract(src1=moon,src2=img1))
cv.waitKey(0)