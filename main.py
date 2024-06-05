import cv2
from datetime import datetime
import cv2.data
from sendSMS import sendSMS

capture=cv2.VideoCapture(0)
face_identifier=cv2.CascadeClassifier(cv2.data.haarcascades+"haarcascade_frontalface_default.xml")
contador=0
while True:
    _,frame=capture.read()
    gray_image=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    faces=face_identifier.detectMultiScale(gray_image,1.3,5)
    if len(faces)>0: 
        x,y,width,height= faces[0]
        cv2.rectangle(frame,(x,y),(x+width, y+height),(255,0,0),5)
        now = datetime.now()
        formatted_date = now.strftime("%Y-%m-%d %H:%M:%S")
        if contador==0 :
            sendSMS("Un ser humano entró en tu cuarto a las: " + str(formatted_date))
        contador=1
    cv2.imshow("camera",frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
capture.release()

cv2.destroyWindow("camera")


