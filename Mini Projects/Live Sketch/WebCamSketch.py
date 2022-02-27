import cv2 as cv

capture = cv.VideoCapture(0)  # turn on webcam of device


def dodge(x, y):
    return cv.divide(x, y, scale=256)

while True:
    success, img = capture.read()  # read video of webcam frame by frame
    imgGray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)  # convert frame into gray image frame
    imgGrayInv = cv.bitwise_not(imgGray)  # tranform gray image into inverse of gray image
    imgBlur = cv.GaussianBlur(imgGrayInv, ksize=(21, 21), sigmaX=5)  # Apply GaussianBlur
    imgBlurInv = cv.bitwise_not(imgBlur)
    finalImg = dodge(imgGray, imgBlurInv)
    cv.imshow('Sketched Web', finalImg)  # Sketched Image
    cv.imshow('Origianl', img)

    key = cv.waitKey(1)
    if key & 0xff == ord('q'):
        break
capture.release()
cv.destroyAllWindows()
