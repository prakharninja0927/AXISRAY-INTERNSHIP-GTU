import cv2 as cv
from loadModel import CarDetector

# capture frames from a video
capture = cv.VideoCapture('carh.mp4')
cd = CarDetector() # creating object
l1=[]
while capture.isOpened():
    ret, frames = capture.read()
    if ret== False:
        break
    # print(len(frames))
    cars_boxes = cd.detect_cars(frames)
    print(cars_boxes)
    cv.imshow('Detection', frames)
    l1.append(cars_boxes)
    cv.imshow('Detection',frames)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

print(l1)
count = 0
while capture.isOpened():
    ret, frames1 = capture.read()

    x, y, w, h = l1[count]
    cv.rectangle(img=frames1, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=3)
    cv.imshow('Detection',frames1)
    count = count + 1
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
    # for rec in cars_boxes:
    #     x, y, w, h = recq
    #     cv.rectangle(img=frames, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=3)
    # cv.imshow('Detection',frames)
    # if cv.waitKey(1) & 0xFF == ord('q'):
    #     break

capture.release()
cv.destroyAllWindows()