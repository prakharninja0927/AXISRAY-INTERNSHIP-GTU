import cv2 as cv
import numpy as np

# Create blank image using numpy
blank_img = np.zeros((600,600,3), dtype=np.uint8)
# cv.imshow('Blank', blank_img)

# 1. paint the whole image using RGB format
blank_img[:] = 0, 255, 0  # blank[:] is for select all pixels
cv.imshow('Whole Green', blank_img)

# 2. paint certain portion of image (certain pixel)
blank_img[200:300, 200:300] = 0, 0, 255
cv.imshow('Color Portions', blank_img)

blank_img[:] = 0,0,0

# 3. draw rectangle
cv.rectangle(img=blank_img, pt1=(0, 0), pt2=(blank_img.shape[1]//2, blank_img.shape[0]//2), color=(255, 40, 0), thickness = -1)  # cv.FILLED = -1
cv.rectangle(img=blank_img, pt1=(350, 350), pt2=(blank_img.shape[1], blank_img.shape[0]), color=(10, 255, 0), thickness = 2)  # cv.FILLED = -1
# 4. draw circle
cv.circle(img=blank_img, center=(250,250), radius=40 ,color=(0,0,255), thickness = cv.FILLED)
cv.circle(img=blank_img, center=(300,300), radius=40 ,color=(0,255,255), thickness = 2)
# 5. draw a line
cv.line(img=blank_img,pt1=(500,0), pt2=(0,500), thickness=3, color=(200,200,200))
cv.imshow('Shapes',blank_img)

# 6. draw ellipse
cv.ellipse(img=blank_img,center=(400,400),axes=(50,200),angle=0,startAngle=0,endAngle=180,color=(255,255,255),thickness=-1)

# 7. Drawing Polygon
points = np.array([[100,50],[210,250],[300,290],[400,450]], np.int32)
points2 = np.array([[300,250],[410,250],[200,190],[100,50]], np.int32)
cv.polylines(img=blank_img,pts=[points],isClosed=False,color=(255,276,0),thickness=10) # open
cv.polylines(img=blank_img,pts=[points2],isClosed=True,color=(255,26,255),thickness=10) # closed

# Show final Image
cv.imshow('Shapes',blank_img)
cv.waitKey(0)