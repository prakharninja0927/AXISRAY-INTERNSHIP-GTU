import cv2 as cv
import numpy as np

# first, bitwise operators operate in binary manner
blank = np.zeros((300,300),dtype='uint8')

rectangle = cv.rectangle(img=blank.copy(),pt1=(30,30),
                         pt2=(270,270), color=255,thickness=-1)
circle = cv.circle(img=blank.copy(),center=(150,150),radius=150,color=255,thickness=-1)

cv.imshow('Rectangle',rectangle)
cv.imshow('Circle',circle)

# Bitwise AND --> return intersecting regions
bitwise_and =cv.bitwise_and(src1=rectangle,src2=circle)
cv.imshow('Bitwise_and',bitwise_and)

# Bitwise OR --> return non-intersection and intersecting regions (like Union)
bitwise_or = cv.bitwise_or(src1=rectangle,src2=circle)
cv.imshow('Bitwise_OR',bitwise_or)

# Bitwise XOR --> returns non-intersecting regions
bitwise_xor = cv.bitwise_xor(src1=rectangle,src2=circle)
cv.imshow('Bitwise_XOR', bitwise_xor)

# Bitwise NOT
bitwise_not = cv.bitwise_not(src=circle)
cv.imshow('Bitwise_Not',bitwise_not)


if cv.waitKey(20) & 0xFF == ord('d'):
    cv.destroyAllWindows()
cv.waitKey(0)