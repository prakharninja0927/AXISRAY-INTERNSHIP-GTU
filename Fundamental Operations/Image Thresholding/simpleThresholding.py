import cv2 as cv

'''
- Thresholding is binarization of an image that is an image where pixels are
either 0/black or 255/white.
-  In thresholding, each pixel value is compared with the threshold value. 
   If the pixel value is smaller than the threshold, it is set to 0, 
   otherwise, it is set to a maximum value (generally 255). 
Two Types of Thresholding:
1. Simple Thresholding 
2. Adaptive Thresholding

# Simple Thresholding:
For every pixel, the same threshold value is applied. If the pixel value is smaller than the threshold,
it is set to 0, otherwise, it is set to a maximum value.
'''

# Read an image
img = cv.imread('../Resources/Photos/img.png')
# img = cv.imread('../Resources/Photos/img_1.png')
cv.imshow('Original Image',img)
img = cv.cvtColor(img, cv.COLOR_BGR2GRAY)


# 1. Binary Threshold: If pixel intensity is greater than the set threshold, value set to 255, else set to 0 (black).
ret, thresh_binary = cv.threshold(img, 120, 255, cv.THRESH_BINARY)

# 2. Binary Inverted Threshold: Inverted or Opposite case of Binary Threshold(thresh_binary)
ret, thresh_binary_inv = cv.threshold(img, 120, 255, cv.THRESH_BINARY_INV)

# 3. Truncated Threshold: If pixel intensity value is greater than threshold, it is truncated(Shorten) to the threshold.
#  The pixel values are set to be the same as the threshold. All other values remain the same.
ret, thresh_truncated = cv.threshold(img, 120, 255, cv.THRESH_TRUNC)

# 4. THRESH TO ZERO : Pixel intensity is set to 0, for all the pixels intensity, less than the threshold value.
ret, thresh_2Zero = cv.threshold(img, 120, 255, cv.THRESH_TOZERO)

# 5. THRESH TO ZERO Inverted : Inverted or Opposite case of THRESH TO ZERO(thresh_2Zero)
ret, thresh_2Zero_Inv = cv.threshold(img, 120, 255, cv.THRESH_TOZERO_INV)

# Showing outputs
cv.imshow('Binary Threshold', thresh_binary)
cv.imshow('Binary Threshold Inverted', thresh_binary_inv)
cv.imshow('Truncated Threshold', thresh_truncated)
cv.imshow('Set to 0', thresh_2Zero)
cv.imshow('Set to 0 Inverted', thresh_2Zero_Inv)

cv.waitKey(0)
