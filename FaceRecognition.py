# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:10:06 2020

@author: admin
"""
import cv2
import os
import pickle

Base_dir="C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\cv2\\data\\"
image_dir= os.path.join(Base_dir,"testimages")

face_Cascade = cv2.CascadeClassifier("C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalface_alt.xml")

recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read("trainner.yml")

labels={"person_name": 1}
with open("labels.pickle", 'rb')as f:
    orig_labels = pickle.load(f)
    labels = {v:k for k,v in orig_labels.items()}

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_Cascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30, 30),
    )
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        roi_gray= gray[y:y+h,x:x+w]
        roi_color= frame[y:y+h,x:x+w]
        #img_item = "C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\testimages.py" + ".png"
        #cv2.imwrite(img_item,roi_gray)
        id_, conf =recognizer.predict(roi_gray)
        if conf>=45 and conf <= 85:
            print(id_)
            print(labels[id_])
            font = cv2.FONT_HERSHEY_SIMPLEX
            name=labels[id_]
            color= (255,255,255)
            stroke = 2
            cv2.putText(frame,name, (x,y), font, 1, color, stroke, cv2.LINE_AA)
        
        img_item="my_image.png"
        cv2.imwrite(img_item,roi_gray)
        cv2.rectangle(frame, (x, y), (x+w, y+h), (255, 0, 0), 2)
                               #endcord x endcord y color(BGR) strokes
    
       
        
    # Display the resulting frame
    
    cv2.imshow('Video', frame)
    key = cv2.waitKey(1)

    if key == ord('q'): #press Esc to quit
        break

# When everything is done
video_capture.release()
cv2.destroyAllWindows()
