import cv2 as cv
import mediapipe as mp
import os
import glob

# face detection does not involve the face tone or color of image.
folder_dir = "../Resources/Faces/"
extensions = ['png', 'jpg', 'gif', 'jpeg']
images = []
[images.extend(glob.glob(folder_dir + '*' + e)) for e in extensions]

# define model
faceDetection = mp.solutions.face_detection.FaceDetection(0.49)
drawOutput = mp.solutions.drawing_utils

for img in images:
    # read image
    image_name = os.path.basename(img).split(".")[0]
    img = cv.imread(img)

    RGB_img = cv.cvtColor(src=img,code=cv.COLOR_BGR2RGB)

    # now apply image to model
    results = faceDetection.process(image=RGB_img)

    if results.detections:
        for id, box in enumerate(results.detections):
            # print(id,box)
            # print(box.score)
            print(box.location_data.relative_bounding_box)

            # drawOutput.draw_detection(image=img,detection=box)
            bboxT = box.location_data.relative_bounding_box
            image_height,image_width = img.shape[:2]
            bbox = int(bboxT.xmin * image_width) , int(bboxT.ymin * image_height), \
                   int(bboxT.width * image_width), int(bboxT.height * image_height)
            cv.putText(img, text=f'{int(box.score[0] * 100)}%', org=(bbox[0], bbox[1] - 10),
                       fontFace=cv.QT_FONT_NORMAL, fontScale=0.8,
                       color=(0, 255, 0), thickness=1)
            cv.rectangle(img,bbox,(0, 255, 0), 2)

    cv.putText(img=img,text=f'Face Count:{len(results.detections)}',
               org=(30,30),fontFace=cv.FONT_HERSHEY_DUPLEX,fontScale=1,color=(0,255,0))
    cv.imshow(f'{image_name}',img)
cv.waitKey(0)