import cv2 as cv
from matplotlib import pyplot as plt

'''
In this method, instead of a box filter, a Gaussian kernel is used.
Gaussian blurring is highly effective in removing Gaussian noise from an image.
We can create a Gaussian kernel with the function, cv.getGaussianKernel().
->Gaussian filter takes the neighbourhood around the pixel and finds its Gaussian weighted average.
--> here I am taking image in which I have manually added 50% noise....
'''

# read an image
img = cv.imread('../Resources/Photos/noised_park.png')
# cv.imshow('Original Image',img)

# Gaussian Blur using getGaussianKernel() method
gaussian_kernel = cv.getGaussianKernel(ksize=7,sigma=2)
smoothed_img = cv.filter2D(src=img,ddepth=-1,kernel=gaussian_kernel)
smoothed_img2 = cv.sepFilter2D(src=img,ddepth=-1,kernelX=gaussian_kernel,kernelY=gaussian_kernel)
# cv.imshow('getGaussianKernel() ',smoothed_img)
# cv.imshow('getGaussianKernel() 2 ',smoothed_img2)


# Gaussian Blur using conventional GaussianBlur() method
gaussian_blur = cv.GaussianBlur(src=img,ksize=(7,7),sigmaX=0)
# cv.imshow('Gaussian Blur',gaussian_blur)


# I have done this because plt.imshow() shows RGB format
img = cv.cvtColor(src=img, code=cv.COLOR_BGR2RGB)
gaussian_blur = cv.cvtColor(src=gaussian_blur,code=cv.COLOR_BGR2RGB)
smoothed_img = cv.cvtColor(src=smoothed_img,code=cv.COLOR_BGR2RGB)
smoothed_img2 = cv.cvtColor(src=smoothed_img2,code=cv.COLOR_BGR2RGB)

# draw pixel distribution after smoothing
plt.subplot(241), plt.imshow(img),plt.title('Noised Image')
plt.subplot(242), plt.imshow(gaussian_blur),plt.title('Gaussian Blur GaussianBlur()')
plt.subplot(243), plt.imshow(smoothed_img),plt.title('getGaussianKernel() with Filter2D()')
plt.subplot(244), plt.imshow(smoothed_img2),plt.title('getGaussianKernel() with sepFilter2D()')
plt.subplot(245),plt.hist(img.ravel(),256,[0,256],color='red'),plt.xlim([0, 256])
plt.subplot(246),plt.hist(gaussian_blur.ravel(),256,[0,256],color='blue'),plt.xlim([0, 256])
plt.subplot(247),plt.hist(smoothed_img.ravel(),256,[0,256],color='orange'),plt.xlim([0, 256])
plt.subplot(248),plt.hist(smoothed_img2.ravel(),256,[0,256],color='purple'),plt.xlim([0, 256])

plt.show()
#

cv.waitKey(0)