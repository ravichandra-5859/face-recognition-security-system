import smtplib
from email.mime.text import MIMEText#email.mime.text.MIMEText(_text[, _subtype[, _charset]])
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase#email.mime.base.MIMEBase(_maintype(e.g. text or image), _subtype(e.g. plain or gif), **_params(e.g.key/value dictionary))
from email import encoders
import os.path
import cv2
import numpy as np
import time
##import os
from time import sleep

camera0=cv2.VideoCapture(0)
frame_width=int(camera0.get(3))
frame_height=int(camera0.get(4))
out=cv2.VideoWriter('outpy.avi',cv2.VideoWriter_fourcc('M','J','P','G'),10,(frame_width,frame_height))


recognizer = cv2.face_LBPHFaceRecognizer.create()
recognizer.read('trainer.yml')
cascadePath = "data/haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);

font = cv2.FONT_HERSHEY_SIMPLEX

#iniciate id counter
id = 0

# names related to ids: example ==> Marcelo: id=1,  etc
names = ['None', 'RAVICHANDRA', 'ASHOK', 'user3', 'user4', 'user5'] 

# Initialize and start realtime video capture
cam = cv2.VideoCapture(0)
cam.set(3, 640) # set video widht
cam.set(4, 480) # set video height

# Define min window size to be recognized as a face

i=0
count=1
def sendmail():
    email = 'ravichandrapathi926@gmail.com'
    password = 'wnlh nnbi kryr bzgx'
    send_to_email = 'officialravi997@gmail.com'
    subject = 'SECURITY'
    message = 'Unknown Person image'
    file_location = 'thief.jpg'

    msg = MIMEMultipart()#Create the container (outer) email message.
    msg['From'] = email
    msg['To'] = send_to_email
    msg['Subject'] = subject
    '''as.string()  
     |
     +------------MIMEMultipart  
                  |                                                |---content-type  
                  |                                   +---header---+---content disposition  
                  +----.attach()-----+----MIMEBase----|  
                                     |                +---payload (to be encoded in Base64)
                                     +----MIMEText'''
    msg.attach(MIMEText(message, 'plain'))#attach new  message by using the Message.attach

    filename = os.path.basename(file_location)#function returns the tail of the path
    attachment = open(file_location, "rb") #â€œrbâ€ (read binary)
    part = MIMEBase('application', 'octet-stream')#Content-Type: application/octet-stream , image/png, application/pdf
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)#Content-Disposition: attachment; filename="takeoff.png"

    msg.attach(part)

    server = smtplib.SMTP('smtp.gmail.com', 587)# Send the message via local SMTP server.
    server.starttls()# sendmail function takes 3 arguments: sender's address, recipient's address and message to send 
    server.login(email, password)
    text = msg.as_string()
    server.sendmail(email, send_to_email, text)
    server.quit()
    print("Mail sent");
while True:
    ret, image =cam.read()
    #img = cv2.flip(img, -1) # Flip vertically
    gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    
    faces = faceCascade.detectMultiScale( 
        gray,
        scaleFactor = 1.2,
        minNeighbors = 5
       )

    for(x,y,w,h) in faces:
        cv2.rectangle(image, (x,y), (x+w,y+h), (0,255,0), 2)
        id, confidence = recognizer.predict(gray[y:y+h,x:x+w])


        # Check if confidence is less them 100 ==> "0" is perfect match 
        if (confidence < 70):
            id = names[id]
            
            confidence = "  {0}%".format(round(100 - confidence))
            if(count == 1):
                        print('face id:',str(id),' detected')
                        count =2
                        i=0
                                    
        else:
            id = "unknown"
            print('no face detected')
            confidence = "  {0}%".format(round(100 - confidence))
            time.sleep(0.1)
            cv2.imwrite(filename='thief.jpg', img=image)
            print("Image captured")
            for c in range(300):
                ret,frame1=camera0.read()
                out.write(frame1)
                print("video capture")
                cv2.imshow('frame',frame1)
                if cv2.waitKey(27) & 0xFF==ord('q'):
                    break
            sendmail()
            
    ##            arduino.write('1')
##            print("BUZZER ON")
            time.sleep(1)
        cv2.putText(image, str(id), (x+5,y-5), font, 1, (255,255,255), 2)
        cv2.putText(image, str(confidence), (x+5,y+h-5), font, 1, (255,255,0), 1)  
    
    cv2.imshow('camera',image)
    i= i+1
    #print('i: ',int(i))
    if(i == 100):
        #print('i: ',int(i))
        count=1
        i=0

    k = cv2.waitKey(10) & 0xff # Press 'ESC' for exiting video
    if k == 27:
        break

# Do a bit of cleanup
print("\n [INFO] Exiting Program and cleanup stuff")
cam.release()
cv2.destroyAllWindows()
