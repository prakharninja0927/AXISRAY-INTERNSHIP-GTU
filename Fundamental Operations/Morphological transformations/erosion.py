import cv2 as cv
import numpy as np

'''

Erosion involves the removal of pixels ate the edges of the region.
It is also called dual of dilation( A XOR B).
The basic idea of erosion is just like soil erosion only, it erodes away 
the boundaries of foreground object.
working :The kernel slides through the image (as in 2D convolution). 
         A pixel in the original image (either 1 or 0) will be considered 1 only if all 
         the pixels under the kernel is 1, otherwise it is eroded (made to zero).
--> It is used later in Closing operation.
--> It is used prior in Opening operation.         
'''

# read an image
img = cv.resize(src= cv.imread('../Resources/Photos/name1.png'), dsize=(700, 400), interpolation=cv.INTER_CUBIC)
cv.imshow('Original Image',img)

# performing erosion
kernel=np.ones((5,5),np.uint8)
eroded_img = cv.erode(src=img,kernel=kernel,iterations=1)
cv.imshow('Eroded Image',eroded_img)


cv.waitKey(0)