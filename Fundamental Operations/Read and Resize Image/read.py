import cv2 as cv

# reading an image
img = cv.imread('../Resources/Photos/cat.jpg')
cv.imshow('Cat', img)

# print shape of and image
'''
Shape of an image describes height, width and no of color channels present in
an image... Shape gives tuple = ( Height, width, color channels)
index 0 -> height
index 1 -> width
index 2 -> color channels 
'''
dimensions = img.shape
height = img.shape[0]
width = img.shape[1]
color_channels = img.shape[2]

print('Dimensions of an image: ',dimensions)
print('Height of an image', height)
print('Width of an image', width)
print('Color channels present in image', color_channels)

# Note: shape of gray scale image only gives height and width --> ( height, width)
# it does not have any color channels except black/white
cv.waitKey(0)
