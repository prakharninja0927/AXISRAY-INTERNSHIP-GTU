import cv2 as cv
import numpy as np
'''
Any color image is basically consists of multiple color channels
such as Red, Green, Blue call three color channels. Most of the color images are
either in BGR or in RGB format. Opencv allows us to split image into 
its respective color channel.
'''

# Read an image
img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Original Color Image', img)

# let's take one blank image of image size
blank = np.zeros(img.shape[:2],dtype='uint8')

# split image into BGR which is by default readable format of opencv
blue, green, red = cv.split(img)

# Printing shapes of splitted images
print(img.shape)
print(blue.shape)
print(green.shape)
print(red.shape)

# === check it out by uncomment the following code what does it show ====
# cv.imshow('Blue', blue)
# cv.imshow('Green', green)
# cv.imshow('Red', red)

# blank other two color spaces respectively
b = cv.merge([blue,blank,blank])
g = cv.merge([blue,green,blank])
r = cv.merge([blue,blank,red])

# show result
cv.imshow('Blue', b)
cv.imshow('Green', g)
cv.imshow('Red', r)

# Printing shapes of splitted images
# all will show 3 color channels because we have merged splitted image with blank
print(img.shape)
print(b.shape)
print(g.shape)
print(r.shape)

# Merge all color channels and we get back out original image
merged_img = cv.merge([blue, green, red])
cv.imshow('Merged_image', merged_img)

cv.waitKey(0)