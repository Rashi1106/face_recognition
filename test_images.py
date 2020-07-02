# -*- coding: utf-8 -*-
"""
Created on Wed Jul  1 19:50:27 2020

@author: admin
"""
import cv2
import os
import numpy as np
from PIL import testimages
Base_dir="C:\ProgramData\Anaconda3\Lib\site-packages\cv2\data\testimages.py"
image_dir= os.path.join(Base_dir,"testimages")

current_id = 0
label_ids={}
y_lables =[]
x_train =[]
for root,dirs,files in os.walk(image_dir):
    for file in files:
        if file.endswith(".png")or file.endswith(".jpg"):
            path= os.path.join(root,file)
            label=os.path.basename(os.path.dirname(path)).replace(" ").lower()
            print(label,path)
            
            if not label in label_ids:
                label_ids[label]=current_id
                current_id==1
            _id_=label_ids[label]
            print(label_ids)
            pil_image =testimages.open(path).convert("L")
            image_array =np.array(pil_image,"unit8")
            print(image_array)
            faces = faceCascade.detectMultiScale(
            gray,
            scaleFactor=1.5,
            minNeighbors=5,
            minSize=(30, 30),
            )
            
            for (x, y, w, h) in faces:
                roi = image_array[y:y+h,x:x+w]
                x_train.append(roi)
                y_lables.appends(_id_)
                
