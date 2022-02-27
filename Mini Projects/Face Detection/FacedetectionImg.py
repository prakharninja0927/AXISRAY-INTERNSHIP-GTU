import cv2 as cv
import os
import glob

# face detection does not involve the face tone or color of image.
folder_dir = "../Resources/Faces/"
extensions = ['png', 'jpg', 'gif', 'jpeg']
images = []
[images.extend(glob.glob(folder_dir + '*' + e)) for e in extensions]
for img in images:
    # read image
    image_name = os.path.basename(img).split(".")[0]
    img = cv.imread(img)

    gray = cv.cvtColor(src=img,code=cv.COLOR_BGR2GRAY)

    # set classifier: harcascade are more noise sensitive
    classifier = cv.CascadeClassifier('../CascadeClassifiers/faceclassifier_cascade.xml')
    faces_ret = classifier.detectMultiScale(image=gray,scaleFactor=1.1,minNeighbors=20)

    print(f'Number of Faces Found:{len(faces_ret)}')
    faces = len(faces_ret)
    for (x,y,w,h) in faces_ret:
        # print(x,y,w,h)
        cv.rectangle(img=img,pt1=(x,y),pt2=(x+w,y+h),color=(0,255,0),thickness=2)
    cv.putText(img=img,text=f'Face Count:{faces}',
               org=(30,30),fontFace=cv.FONT_HERSHEY_DUPLEX,fontScale=1,color=(0,255,0))
    cv.imshow(f'{image_name}',img)
cv.waitKey(0)