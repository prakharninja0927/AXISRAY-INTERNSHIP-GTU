import cv2 as cv
import datetime as dt

# Read video
capture = cv.VideoCapture(0,cv.CAP_DSHOW)
# cmp = cv.VideoCapture('../Resources/Videos/dog.mp4')

print("width:",capture.get(cv.CAP_PROP_FRAME_WIDTH)) # returns frame width of video
print("Height:",capture.get(cv.CAP_PROP_FRAME_HEIGHT)) # returns frame height of video

# change width and height called setting camera parameters
capture.set(cv.CAP_PROP_FRAME_WIDTH,1080)
capture.set(cv.CAP_PROP_FRAME_HEIGHT,720)
print("New width:",capture.get(cv.CAP_PROP_FRAME_WIDTH)) # returns frame width of video
print("New Height:",capture.get(cv.CAP_PROP_FRAME_HEIGHT)) # returns frame height of video

'''
isOpened() method check if file path is correct and if it is it returns true and then and then
only while loop will run else for wrong path or argument it returns false try cv.VideoCapture(8)
so value of isOpened() will be False.
'''

# Show text on videos
while (capture.isOpened()):
    isTrue, frame = capture.read()
    if isTrue:
        gray_frame = frame #cv.cvtColor(src=frame, code=cv.COLOR_BGR2GRAY)
        date_time = str(dt.datetime.now())
        text = 'width: '+str(capture.get(cv.CAP_PROP_FRAME_WIDTH)) +' Height: '+str(capture.get(cv.CAP_PROP_FRAME_HEIGHT))
        cv.putText(img=gray_frame, text=text, fontFace=cv.FONT_HERSHEY_TRIPLEX,org=(10,50),
                   fontScale=1, color=(0,0,0),thickness=1,lineType= cv.LINE_AA)
        cv.putText(img=gray_frame, text=date_time, fontFace=cv.FONT_HERSHEY_TRIPLEX, org=(750, 50),
                   fontScale=1, color=(255, 255, 255), thickness=1, lineType=cv.LINE_AA)
        cv.rectangle(img=gray_frame,pt1=(150,150),pt2=(500,500),color=(0,255,255),thickness=2,lineType=cv.LINE_4)
        cv.line(img=gray_frame,pt1=(150,150),pt2=(500,500),color=(0,0,0),thickness=3,lineType=cv.LINE_AA)
        cv.arrowedLine(img=gray_frame,pt1=(150,500),pt2=(500,150),color=(0,0,0),thickness=3)

        cv.circle(img=gray_frame,center=(500,500),radius=200,color=(0,255,0),thickness=5,lineType=cv.LINE_8)

        cv.imshow('Video', gray_frame)

        if cv.waitKey(20) & 0xFF == ord('d'):
            break

capture.release()
cv.destroyAllWindows()
