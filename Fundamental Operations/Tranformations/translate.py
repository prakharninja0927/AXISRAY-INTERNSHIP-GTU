import cv2 as cv
import numpy as np

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

# Translation : is shifting an image along the X and Y axis (left-right, up-down)
'''
Translation refers to the rectilinear shift of an object  i.e. an image from one location to another
Matrix = [1, 0, X]
         [0, 1, y]
Advantages/application of image translation are:
- Hiding a part of the image
- Cropping an image
- Shifting an image
- Animating an image using image translations in loop.         
'''
# -x --> Left
# -y --> Up
# +x --> Right
# +y --> Down
def translateImage(img, x, y):
    # generate translation matrix using numpy library
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (img.shape[1], img.shape[0])

    return cv.warpAffine(src=img, M=transMat, dsize=dimensions)

translatedimg = translateImage(img, -100, 100)  # x and y are in pixels
cv.imshow('Translated Image', translatedimg)

cv.waitKey(0)