import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

# read an image
img = cv.imread('../Resources/Photos/noised_park.png')

# 2D convolution
kernel = np.ones((5,5),np.float32)/25 # normalized 2D convolution filter
convol_2D = cv.filter2D(img,-1,kernel)

# averaging blurring (both produces same output normalised
norm_blur = cv.blur(src=img, ksize=(7,7))
norm_blur = cv.boxFilter(src=img,ddepth=0,ksize=(7,7),normalize=True)

# Gaussian blur
gaussian_blur = cv.GaussianBlur(src=img,ksize=(7,7),sigmaX=0)

# median blur
median_filter = cv.medianBlur(src=img,ksize=7)

# bilateral Filter
bilateral_blur = cv.bilateralFilter(src=img,d=7,sigmaSpace=75,sigmaColor=100)


# I have done this because plt.imshow() shows RGB format
img = cv.cvtColor(src=img, code=cv.COLOR_BGR2RGB)
convol_2D = cv.cvtColor(src=convol_2D,code=cv.COLOR_BGR2RGB)
norm_blur = cv.cvtColor(src=norm_blur,code=cv.COLOR_BGR2RGB)
gaussian_blur = cv.cvtColor(src=gaussian_blur,code=cv.COLOR_BGR2RGB)
median_filter = cv.cvtColor(src=median_filter,code=cv.COLOR_BGR2RGB)
bilateral_blur = cv.cvtColor(src=bilateral_blur,code=cv.COLOR_BGR2RGB)



# draw pixel distribution after smoothing
plt.subplot(261), plt.imshow(img),plt.title('Noised Image')
plt.subplot(262), plt.imshow(convol_2D),plt.title('2D Convolutionised Image')
plt.subplot(263), plt.imshow(norm_blur),plt.title('Averaging')
plt.subplot(264), plt.imshow(gaussian_blur),plt.title('Gaussian blur')
plt.subplot(265), plt.imshow(median_filter),plt.title('Median blur')
plt.subplot(266), plt.imshow(bilateral_blur),plt.title('bilateral Filter')

plt.subplot(267),plt.hist(img.ravel(),256,[0,256],color='red'),plt.xlim([0, 256])
plt.subplot(268),plt.hist(convol_2D.ravel(),256,[0,256],color='blue'),plt.xlim([0, 256])
plt.subplot(269),plt.hist(norm_blur.ravel(),256,[0,256],color='green'),plt.xlim([0, 256])
plt.subplot(2,6,10),plt.hist(gaussian_blur.ravel(),256,[0,256],color='purple'),plt.xlim([0, 256])
plt.subplot(2,6,11),plt.hist(median_filter.ravel(),256,[0,256],color='orange'),plt.xlim([0, 256])
plt.subplot(2,6,12),plt.hist(bilateral_blur.ravel(),256,[0,256],color='gray'),plt.xlim([0, 256])

plt.show()

cv.waitKey(0)