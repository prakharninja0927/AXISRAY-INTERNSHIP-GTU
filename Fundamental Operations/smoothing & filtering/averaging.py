import cv2 as cv
import matplotlib.pyplot as plt
'''
we generally smooth an image when it contains a lot of noise with intend to
reduce noise of the image for better output these noise may be occurred 
due to camera sensors or environment in which image is taken / problem in
lighting.
To smooth or blur an image we need a window which is also called kernel matrix.
Blurring process if applied to middle pixel as a result of around pixels(surrounding pixels)
'''

'''
Averaging is done by convolving an image with a normalized box filter. It simply takes the average of all 
the pixels under the kernel area and replaces the central element. 

--> here I am taking image in which I have manually added 50% noise....
'''
# read an image
img = cv.imread('../Resources/Photos/noised_park.png')
# cv.imshow('Original Image',img)

# Normalized smoothing or blurring (Averaging) both blur method generate same output
norm_blur = cv.blur(src=img, ksize=(7,7))
norm_blur = cv.boxFilter(src=img,ddepth=0,ksize=(7,7),normalize=True)
# cv.imshow('Averaging(Normalized)',norm_blur)


# not Normalized smoothing (Averaging)

# cv.imshow('Averaging(Not Normalized)',nnorm_blur)
nnorm_blur = cv.boxFilter(src=img,ddepth=0,ksize=(7,7),normalize=False)

# I have done this because plt.imshow() shows RGB format
img = cv.cvtColor(src=img, code=cv.COLOR_BGR2RGB)
norm_blur = cv.cvtColor(src=norm_blur,code=cv.COLOR_BGR2RGB)

# draw pixel distribution after smoothing normalised
plt.subplot(221), plt.imshow(img),plt.title('Noised Image')
plt.subplot(222), plt.imshow(norm_blur),plt.title('Average Filtered Image')
plt.subplot(223),plt.hist(img.ravel(),256,[0,256]),plt.xlim([0, 256])
plt.subplot(224),plt.hist(norm_blur.ravel(),256,[0,256],color='r'),plt.xlim([0, 256])
plt.show()

cv.waitKey(0)