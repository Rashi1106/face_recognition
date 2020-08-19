#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 17 19:27:45 2020

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
Base_dir="/home"
image_dir= os.path.join(Base_dir,"/home/rashi/faces")

storage= base.storage()
path_on_cloud ="/Device_id_known_faces/"

ref = firebase.FirebaseApplication('https://fir-55139.firebaseio.com/', None)
result = ref.get('/All_devices/-MEMxh1nFvXai-nQqOZI/Known_faces/', None)
print (result) 
keys=[]

values=[]
for key, val in result.items():
	keys.append(key)
	values.append(val)
print(keys)

direc = list(filter(lambda x: os.path.isdir(image_dir+'/'+x), os.listdir(image_dir)))
direc= list(map(lambda x: x.title(),direc))
print(direc)
print(values,'aaa')

#images = list(filter(lambda i: os.path.exists(direc+'/' i ),os.walk(image_dir)))
#print(images)
       
temp =list(keys)
for d in direc:
     temp.remove(d)
     print("removed",d)
print(temp)
if len(temp)>0:
    for newdir in temp:
        path=image_dir+"/"+newdir		
        direc.append(newdir)		
        try:
            os.mkdir(path)
        except OSError as error:
            print(error)		
print (direc)				
	


       
								  
				
				
			              
#storage.child(path_on_cloud).put(path_local)
#storage.child(path_on_cloud).download("/home/rashi/faces/0000000.jpeg")			
