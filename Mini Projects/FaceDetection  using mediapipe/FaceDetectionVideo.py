import cv2 as cv
import mediapipe as mp
import time
# turn on webcam of device or read video
capture = cv.VideoCapture(0)

# define model
faceDetection = mp.solutions.face_detection.FaceDetection(0.49)
drawOutput = mp.solutions.drawing_utils

pTime = 0
while capture.isOpened():
    isTrue, frame = capture.read()
    RGB_frame = cv.cvtColor(src=frame, code=cv.COLOR_BGR2RGB)

    # now apply image to model
    results = faceDetection.process(image=RGB_frame)

    if results.detections:
        for id, box in enumerate(results.detections):
            # print(id,box)
            # print(box.score)
            # print(box.location_data.relative_bounding_box)
            # drawOutput.draw_detection(image=img,detection=box)
            bboxT = box.location_data.relative_bounding_box
            image_height,image_width = frame.shape[:2]
            bbox = int(bboxT.xmin * image_width) , int(bboxT.ymin * image_height), \
                   int(bboxT.width * image_width), int(bboxT.height * image_height)
            cv.rectangle(frame,bbox,(0, 255, 0), 2)
            cv.putText(frame, text=f'{int(box.score[0] * 100)}%',org = (bbox[0],bbox[1]-20),fontFace=cv.FONT_HERSHEY_SIMPLEX,fontScale=1,
                       color=(0, 255, 0), thickness=2)

        cv.putText(img=frame,text=f'Face Count:{len(results.detections)}',
               org=(30,30),fontFace=cv.FONT_HERSHEY_DUPLEX,fontScale=1,color=(0,255,0))
    else:
        cv.putText(img=frame, text=f'Face Count:{0}',
                   org=(30, 30), fontFace=cv.FONT_HERSHEY_DUPLEX, fontScale=1, color=(0, 255, 0))

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv.putText(img=frame,text=f'FPS:{int(fps)}',
               org=(20,70),fontFace=cv.FONT_HERSHEY_DUPLEX,fontScale=1,color=(0,255,0))
    cv.imshow('Output', frame)

    if cv.waitKey(1) & 0xFF == ord('d'):
        break
capture.release()
cv.destroyAllWindows()