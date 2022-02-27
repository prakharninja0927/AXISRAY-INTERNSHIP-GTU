import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
'''
Best method to Apply custom-made filters to images (2D convolution)
while others are various low pass filters
The operation works like this: keep this kernel a pixel, add all 
the  pixels below this kernel, take the average, and replace the central 
pixel with the new average value.This operation is continued for all the 
pixels in the image.

--> here I am taking image in which I have manually added 50% noise....
'''
# read an image
img = cv.imread('../Resources/Photos/noised_park.png')
# cv.imshow('Original Image',img)

# Apply 2D Convolution operations
kernel = np.ones((5,5),np.float32)/25 # normalized 2D convolution filter
non_kernel = np.ones((5,5),np.float32) # non-normalized 2D Convolution Filter
convol_2D = cv.filter2D(img,-1,kernel)
non_convol_2D = cv.filter2D(img,-1,non_kernel)
# cv.imshow('2D Convolutionaized Image(Normalized)',convol_2D)
# cv.imshow('2D Convolutionaized Image(non-Normalized)',non_convol_2D)


# I have done this because plt.imshow() shows RGB format
img = cv.cvtColor(src=img, code=cv.COLOR_BGR2RGB)
convol_2D = cv.cvtColor(src=convol_2D,code=cv.COLOR_BGR2RGB)

# draw pixel distribution after smoothing
plt.subplot(221), plt.imshow(img),plt.title('Noised Image')
plt.subplot(222), plt.imshow(convol_2D),plt.title('2D Convolutionised Image')
plt.subplot(223),plt.hist(img.ravel(),256,[0,256],color='red'),plt.xlim([0, 256])
plt.subplot(224),plt.hist(convol_2D.ravel(),256,[0,256],color='blue'),plt.xlim([0, 256])
plt.show()

cv.waitKey(0)