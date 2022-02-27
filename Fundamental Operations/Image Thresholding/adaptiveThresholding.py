import cv2 as cv
'''
Adaptive Thresholding:
The Adaptive thresholding has some advantages over the simple thresholding.
In the simple thresholding, the threshold value is global,
i.e., it is same for all the pixels in the image.In adaptive thresholding,
the threshold value is calculated for smaller regions and therefore, 
there will be different threshold values for different regions. 
So, we can get different thresholds for different regions of the same image 
and it gives us better results for images with varying illumination.
'''

# Read an image
img = cv.imread('../Resources/Photos/sudoku.png')
img = cv.cvtColor(src=img,code=cv.COLOR_BGR2GRAY)
cv.imshow('Original Image',img)

# lets first see what global thresholding(simple) will do with image
ret, thresh_binary = cv.threshold(img, 120, 255, cv.THRESH_BINARY)
cv.imshow('Binary Threshold', thresh_binary)

'''
Let's look after all parameters for Adaptive Thresholding

-->src − An object of the class Mat representing the source (input) image.
-->maxValue − A variable of double type representing the value that is to be given 
              if pixel value is more than the threshold value.
-->adaptiveMethod − A variable of integer the type representing the adaptive method to be used. 
                    This will be either of the following two values
                          1.  ADAPTIVE_THRESH_MEAN_C − threshold value is the mean of neighborhood area.
                          2.  ADAPTIVE_THRESH_GAUSSIAN_C − threshold value is the weighted sum of neighborhood 
                                                            values where weights are a Gaussian window.
-->thresholdType − A variable of integer type representing the type of threshold to be used.
-->blockSize − A variable of the integer type representing size of the pixelneighborhood used 
                to calculate the threshold value.
-->C − A variable of double type representing the constant used in the both methods 
      (subtracted from the mean or weighted mean).                
'''
# 1. ADAPTIVE THRESH MEAN C: The threshold value is the mean of the neighbourhood area minus the constant C.
adaptive_mean = cv.adaptiveThreshold(src=img,maxValue=255,adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C,thresholdType=cv.THRESH_BINARY
                           , blockSize=11,C=2)
adaptive_mean_inv = cv.adaptiveThreshold(src=img,maxValue=255,adaptiveMethod=cv.ADAPTIVE_THRESH_MEAN_C,thresholdType=cv.THRESH_BINARY_INV
                           , blockSize=11,C=2)
cv.imshow('Adaptive Mean',adaptive_mean)
cv.imshow('Adaptive Mean Inverse',adaptive_mean_inv)

# 2.ADAPTIVE_THRESH_GAUSSIAN_C: The threshold value is a gaussian-weighted sum of the neighbourhood values minus the constant C.
adaptive_gaussian = cv.adaptiveThreshold(src=img,maxValue=255,adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C,thresholdType=cv.THRESH_BINARY
                           , blockSize=11,C=2)
adaptive_gaussian_inv = cv.adaptiveThreshold(src=img,maxValue=255,adaptiveMethod=cv.ADAPTIVE_THRESH_GAUSSIAN_C,thresholdType=cv.THRESH_BINARY_INV
                           , blockSize=11,C=2)
cv.imshow('Adaptive Gaussian Inverse',adaptive_gaussian_inv)

cv.waitKey(0)