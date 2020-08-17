#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 14:57:20 2020

@author: rashi
"""
import os
import os.path
import pyrebase
from firebase import firebase
from firebase.firebase import FirebaseApplication

config = {
	"apiKey": "AIzaSyBBYu__9D-xouOF1AYO5kmq4NPCJyfx-9E",
    "authDomain": "fir-55139.firebaseapp.com",
    "databaseURL": "https://fir-55139.firebaseio.com",
    "projectId": "fir-55139",
    "storageBucket": "fir-55139.appspot.com",
    "messagingSenderId": "564786652598",
    "appId": "1:564786652598:web:ebaf803b5b42b0da67cd17",
    "measurementId": "G-WZRTVB6691"
	}

base= pyrebase.initialize_app(config)
#labels ={iname: 1}
Base_dir="/home"
image_dir= os.path.join(Base_dir,"/home/rashi/faces")

storage= base.storage()
path_on_cloud ="/Device_id_known_faces/"
path_local = "/home/rashi/faces/"

ref = firebase.FirebaseApplication('https://fir-55139.firebaseio.com/', None)
result = ref.get('/All_devices/-MEMxh1nFvXai-nQqOZI/Known_faces/', None)
print (result)
keys=[]
values=[]
for key, val in result.items():
	keys.append(key)
	values.append(val)
	#print(' {0} : {1}'.format(key, val)) 
	print(keys)
	print(values)     	
direc = [] 
imgs=[]

for root,dirs,files in os.walk(image_dir):
    for directory in dirs:
        direc.append(directory)  
        res= [x for x in keys + direc if x not in keys or x not in direc]
        print(res)
        for i,vall in enumerate(keys)  :
            print(i,'',vall)       		
            if os.path.exists('/home/rashi/faces/')==True:            
			#direc.append(directory)
                print("Directory " , directory ," already exists")
            else:	                  
                os.mkdir(res)
                direc.append(directory)
                print("Directory " , directory ," Created ")
         						               				      		
    for file in files:
        if file.endswith(".jpeg"):           
            if [values]== [imgs]:
                path = os.path.join(root,file)
                labels = os.path.basename(directory)
                print(file)
            else:               
                storage.child(path_on_cloud).download("/home/rashi/faces/0000000.jpeg")

	
             
    
#storage.child(path_on_cloud).put(path_local)
#storage.child(path_on_cloud).download("/home/rashi/faces/0000000.jpeg")			
