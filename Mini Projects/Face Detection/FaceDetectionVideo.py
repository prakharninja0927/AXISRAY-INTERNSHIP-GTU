import cv2 as cv

# turn on webcam of device
capture = cv.VideoCapture(0)
classifier = cv.CascadeClassifier('../CascadeClassifiers/faceclassifier_cascade.xml')
# read video which is being captured by webcam
while capture.isOpened():
    isTrue, frame = capture.read()
    gray = cv.cvtColor(src=frame, code=cv.COLOR_BGR2GRAY)

    # detecting faces
    faces_ret = classifier.detectMultiScale(image=gray, scaleFactor=1.1, minNeighbors=20)
    faces = len(faces_ret)

    for (x, y, w, h) in faces_ret:
        # print(x,y,w,h)
        cv.rectangle(img=frame, pt1=(x, y), pt2=(x + w, y + h), color=(0, 255, 0), thickness=2)

    cv.putText(img=frame, text=f'Face Count:{faces}',
               org=(30, 30), fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0, 255, 0))
    cv.imshow('Webcam', frame)
    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cv.destroyAllWindows()