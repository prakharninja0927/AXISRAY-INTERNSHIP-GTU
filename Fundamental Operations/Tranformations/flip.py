import cv2 as cv

img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Park', img)

''' flipping the image
    if flipCode = 0 ---> flip vertically 
    if flipCode = 1 ---> flip horizontally
    if flipCode = -1 ---> flip both vertically and horizontally

'''

# flip image vertically
flip_img_v = cv.flip(src=img, flipCode=0)
cv.imshow('flipped Image Vertically', flip_img_v)

# flip image horizontally
flip_img_h = cv.flip(src=img, flipCode=1)
cv.imshow('flipped Image horizontally', flip_img_h)

# flip image both vertically and horizontally
flip_img = cv.flip(src=img, flipCode=-1)
cv.imshow('flipped Image vertically and horizontally', flip_img)
cv.waitKey(0)
