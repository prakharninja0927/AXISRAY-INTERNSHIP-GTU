import cv2 as cv


'''There are more than 346 color-space conversion methods available in OpenCV
Mostly being used are BGR, RGB, HSV, GrayScale ..
'''
flags = [i for i in dir(cv) if i.startswith('COLOR_')]
print( len(flags ))

# read Image
img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Original(BGR Format)',img)

# convert image to gray
gray_img = cv.cvtColor(src=img,code=cv.COLOR_BGR2GRAY)
cv.imshow('Grayscale',gray_img)

# Convert to RGB format
RGB_img = cv.cvtColor(src=img,code=cv.COLOR_BGR2RGB)
cv.imshow('RGB Format',RGB_img)

# Convert to HSV format
hsv_img = cv.cvtColor(src=img,code=cv.COLOR_BGR2HSV)
cv.imshow('HSV Format',hsv_img)

# Convert to HLS format
hls_img = cv.cvtColor(src=img,code=cv.COLOR_BGR2HLS)
cv.imshow('Hls Format',hls_img)

# Convert to XYZ format
XYZ_img = cv.cvtColor(src=img,code=cv.COLOR_BGR2XYZ)
cv.imshow('XYZ Format',XYZ_img)

''' There can be more other conversion but the method will remain same for all of them'''
cv.waitKey(0)



