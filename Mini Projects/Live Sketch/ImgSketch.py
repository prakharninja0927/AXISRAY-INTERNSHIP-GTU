import cv2 as cv
import matplotlib.pyplot as plt

# read image
img = cv.imread('../Resources/Images/virat.jpg')
cv.imshow('Original Image',img)

# convert image to gray scale and then take its inverse
imgGray = cv.cvtColor(src=img,code=cv.COLOR_BGR2GRAY)
imgGrayInv = cv.bitwise_not(src=imgGray)


# Apply gaussian blur to inversed image
imgBlur = cv.GaussianBlur(src=imgGrayInv,ksize=(21,21),sigmaX=2.3)

# Inverse blur image
imgBlurInv = cv.bitwise_not(imgBlur)

finalImg = cv.divide(src1=imgGray,src2=imgBlurInv,scale=256)
cv.imshow('Sketched Image',finalImg)

cv.waitKey(0)