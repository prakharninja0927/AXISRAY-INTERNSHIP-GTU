import cv2 as cv
from matplotlib import pyplot as plt
'''
 takes the median of all the pixels under the kernel area and the central element is replaced with this median value. 
 This is highly effective against salt-and-pepper noise in an image.

--> here I am taking image in which I have manually added 50% noise....
'''
# read an image
img = cv.imread('../Resources/Photos/noised_park.png')
# cv.imshow('Original Image',img)

median_filter = cv.medianBlur(src=img,ksize=7)
# cv.imshow('Median Filter',median_filter)



# I have done this because plt.imshow() shows RGB format
img = cv.cvtColor(src=img, code=cv.COLOR_BGR2RGB)
median_filter = cv.cvtColor(src=median_filter,code=cv.COLOR_BGR2RGB)



# draw pixel distribution after smoothing
plt.subplot(221), plt.imshow(img),plt.title('Noised Image')
plt.subplot(222), plt.imshow(median_filter),plt.title('Median Filtered Image')
plt.subplot(223),plt.hist(img.ravel(),256,[0,256],color='red'),plt.xlim([0, 256])
plt.subplot(224),plt.hist(median_filter.ravel(),256,[0,256],color='blue'),plt.xlim([0, 256])
plt.show()

cv.waitKey(0)