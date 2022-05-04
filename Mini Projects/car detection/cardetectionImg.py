import cv2 as cv
from loadModel import CarDetector

cd = CarDetector() # creating object
# img = cv.imread('../Resources/Photos/car2.jpg')
img = cv.imread('images/test.jpg')
# img = cv.resize(src=img,dsize=(800,750),interpolation=cv.INTER_AREA)
cars_boxes = cd.detect_cars(img) # format :[arr1,arr2]
car_count = len(cars_boxes)

for rec in cars_boxes:
    x,y,w,h = rec
    cv.rectangle(img=img, pt1=(x, y), pt2=(x + w, y + h),color=(0, 255, 0), thickness=3)
    text = f'total cars in image is {car_count}'
    cv.putText(img=img,text=text,org=(20,30),fontFace=0,fontScale=1,
               color=(0,0,255),thickness=2)

cv.imshow("Cars", img)
cv.waitKey(0)

