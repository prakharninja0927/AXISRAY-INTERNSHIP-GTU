import cv2 as cv

# read image 1
sky = cv.resize(src=cv.imread('../Resources/Photos/sky.jpeg'),dsize=(600,600),interpolation=cv.INTER_CUBIC)
moon = cv.resize(src=cv.imread('../Resources/Photos/moon.jpeg'),dsize=(600,600),interpolation=cv.INTER_CUBIC)
cv.imshow('Sky',sky)
cv.imshow('Moon',moon)

# add images
'''This directly adds up image pixels in the two images. '''
simple_add = cv.add(src1=moon,src2=sky)
cv.imshow('Add',simple_add)

# add with weights
'''But adding the pixels is not an ideal situation. So, we use cv2.addweighted().
 Remember, both images should be of equal size and depth. '''
'''
This is also image addition, but different weights are given to images in order to give a feeling of blending or transparency. 
Images are added as per the equation below:
g(x)=(1−α)f0(x)+αf1(x)
'''

weightedSum = cv.addWeighted(src1=sky,alpha=0.6,src2=moon,beta=0.4,gamma=0.5)
cv.imshow('Weigthed Image',weightedSum)
'''
alpha = Weight of the first input image elements to be applied to the final image
beta = Weight of the second input image elements to be applied to the final image 
gamma = Measurement of light 
'''
cv.waitKey(0)