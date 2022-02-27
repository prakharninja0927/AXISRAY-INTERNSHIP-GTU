import cv2 as cv

# Read Image
img = cv.imread('../Resources/Photos/park.jpg')
cv.imshow('Original Image',img)

def rotate(img, angle, rotPoint=None):
    (img_height,img_width) = img.shape[:2]
    if rotPoint==None:
        rotPoint = (img_width//2,img_height//2)
    # get rotation matrix
    ''' 
    center: Center of rotation
    angle(θ): Angle of Rotation. 
        Angle is positive for anti-clockwise and negative for clockwise.
    scale: scaling factor which scales the image'''
    rotMat = cv.getRotationMatrix2D(center=rotPoint,angle=angle,scale=1.0)

    return cv.warpAffine(src=img, M=rotMat, dsize=(img_width,img_height))

rotatedimg = rotate(img, -45) # clockwise
cv.imshow('Rotated Image(Clock Wise)', rotatedimg)

anti_clock = rotate(img,45) # Anti-clockwise
cv.imshow('Rotated Image(Anti-Clock Wise)',anti_clock)

# rotate image but not from center
myrotate = rotate(img,45,(0,0))
cv.imshow('My Rotate',myrotate)

cv.waitKey(0)