import cv2 as cv

# Read Image
img = cv.imread('../Resources/Photos/cats.jpg')
cv.imshow('Original Image', img)


def cropImg(img, scale1=0.15, scale2=0.85):
    height, width = img.shape[:2]
    if scale1 > scale2:
        print(" Scale1 must be less than scale 2")
    else:
        startRow = int(height * scale1)
        startCol = int(width * scale1)
        endRow = int(height * scale2)
        endCol = int(width * scale2)
        return img[startRow:endRow, startCol:endCol]

# default scales
cropped_image = cropImg(img)
cv.imshow('Cropped Image', cropped_image)

# userdefined scale
custom_crop = cropImg(img,0.20,0.50)
cv.imshow('Custom cropped Image', custom_crop)

# what is pass wrong parameters
custom_crop1 = cropImg(img,0.80,0.10)
# cv.imshow('Custom cropped Image', custom_crop1)  # this will arise an error if scale1 > scale2
cv.waitKey(0)
