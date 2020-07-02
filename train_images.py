# -*- coding: utf-8 -*-
"""
Created on Thu Jul  2 18:33:11 2020

@author: admin
"""

import cv2
import os
import numpy as np
from PIL import Image
import pickle

Base_dir="C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\cv2\\data\\"
image_dir= os.path.join(Base_dir,"testimages")

# Load the cascade
face_cascade = cv2.CascadeClassifier('C:\\ProgramData\\Anaconda3\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_altq.xml')
recognizer = cv2.face.LBPHFaceRecognizer_create()

current_id=0
label_ids={}
y_labels=[]
x_train=[]


for root,dirs,files in os.walk(image_dir):
    for file in files:
        if file.endswith(".png")or file.endswith(".jpg"):
            path= os.path.join(root,file)
            label=os.path.basename(root)
            #print(label,path)
            
            if not label in label_ids:
                label_ids[label] = current_id
                current_id += 1
            id_ = label_ids[label]
            #print(label_ids)
            pil_image=Image.open(path).convert("L")#grayscale
            image_array=np.array(pil_image,"uint8")#converting in numpy array
           # print(image_array)
            
            #Read the input image
            img = cv2.imread(path)
            # Convert into grayscale
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            # Detect faces
            faces = face_cascade.detectMultiScale(gray, 1.5, 5)
            
            # Draw rectangle around the faces
            for (x, y, w, h) in faces:
                roi= image_array[y:y+h, x:x+w]
                x_train.append(roi)
                y_labels.append(id_)
                cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)
            # Display the output
                #cv2.imshow('img', img)
            cv2.waitKey()
            
#print(y_lables)
#print(x_train)

with open("labels.pickle", 'wb')as f:
    pickle.dump(label_ids, f)
    
recognizer.train(x_train, np.array(y_labels))
recognizer.save("trainner.yml")


            
            
            
            
            