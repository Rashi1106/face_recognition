# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 15:10:06 2020

@author: admin
"""
import cv2
import os

Base_dir="C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\testimages.py"
image_dir= os.path.join(Base_dir,"testimages")
faceCascade = cv2.CascadeClassifier("C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\haarcascade_frontalcatface.xml")

video_capture = cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = faceCascade.detectMultiScale(
        gray,
        scaleFactor=1.5,
        minNeighbors=5,
        minSize=(30, 30),
    )
    
    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        roi_gray= gray[y:y+h,x:x+w]
        roi_color= frame[y:y+h,x:x+w]
        img_item = "C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\testimages.py" + ".png"
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
