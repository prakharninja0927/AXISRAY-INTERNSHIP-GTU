import cv2 as cv
from matplotlib import pyplot as plt
'''
It is highly effective in noise removal while keeping edges sharp. 
But the operation is slower compared to other filters.
filter is a function of space alone, that is, nearby pixels are considered while filtering. 
It doesn't consider whether pixels have almost the same intensity. It doesn't consider whether 
a pixel is an edge pixel or not.  So it blurs the edges also, which we don't want to do. 

--> here I am taking image in which I have manually added 50% noise....
'''
# read an image
img = cv.imread('../Resources/Photos/noised_park.png')
# cv.imshow('Original Image',img)
# Bilateral Blurring
'''
d          ---> Diameter of each pixel neighborhood that is used during filtering. 
sigmaColor ---> Filter sigma in the color space. 
                A larger value of the parameter means that farther colors 
                within the pixel neighborhood (see sigmaSpace) will be mixed together, 
                resulting in larger areas of semi-equal color.
sigmaSpace --->	Filter sigma in the coordinate space. A larger value of the parameter means 
                that farther pixels will influence each other as long as their colors are close 
                enough (see sigmaColor ). When d>0, it specifies the neighborhood size regardless 
                of sigmaSpace. Otherwise, d is proportional to sigmaSpace.
'''
bilateral_blur = cv.bilateralFilter(src=img,d=9,sigmaSpace=75,sigmaColor=100)
# cv.imshow('Bilateral Filtered Image',bilateral_blur)

# I have done this because plt.imshow() shows RGB format
img = cv.cvtColor(src=img, code=cv.COLOR_BGR2RGB)
bilateral_blur = cv.cvtColor(src=bilateral_blur,code=cv.COLOR_BGR2RGB)


# draw pixel distribution after smoothing
plt.subplot(221), plt.imshow(img),plt.title('Noised Image')
plt.subplot(222), plt.imshow(bilateral_blur),plt.title('Bilateral Filtered Image')
plt.subplot(223),plt.hist(img.ravel(),256,[0,256],color='red'),plt.xlim([0, 256])
plt.subplot(224),plt.hist(bilateral_blur.ravel(),256,[0,256],color='blue'),plt.xlim([0, 256])
plt.show()

cv.waitKey(0)