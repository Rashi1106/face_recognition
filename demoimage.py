#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 14:57:20 2020

@author: rashi
"""
#import pyrebase
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

#firebase= pyrebase.initialize_app(config)
'''firebase = firebase.FirebaseApplication('https://fir-55139.firebaseio.com/', None)
result = firebase.get('/All_devices/-MEMxh1nFvXai-nQqOZI/Known_faces/', None)
print (result)
'''
#val gsReference = storage.getReferenceFromUrl('gs://fir-55139.appspot.com/')
#val httpsReference = storage.getReferenceFromUrl(  
#"https://console.firebase.google.com/project/fir-55139/storage/fir-55139.appspot.com/files~2F") 
firebase = firebase.FirebaseApplication('gs://fir-55139.appspot.com', None)
result = firebase.get('/Device_id_known_faces/', None)
print (result)
     
#storage= firebase.storage()
#path_on_cloud ="device_id_known_face/images/alia"
#path_local = "/home/rashi/myimg.jpeg"
#storage.child(path_on_cloud).put(path_local)
#storage.child(path_on_cloud).download("test_download.jpeg")

