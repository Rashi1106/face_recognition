import os
from datetime import datetime
import pyrebase
from firebase import firebase

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
rec_dir= os.path.join(Base_dir,"/home/rashi/audio_recordings/")

storage= base.storage()
path_on_cloud ="recordings/"
path_local= rec_dir

rec_in_direc=list(os.listdir(rec_dir+"/"))
print(rec_in_direc)

timestring= int(datetime.now().strftime("%d%m%Y%H%M"))
print(timestring)
ref = firebase.FirebaseApplication('https://fir-55139.firebaseio.com/', None)     	  	 

#uploading rec_audio & image to firebase storage
for file in rec_in_direc:
    if file.endswith(".wav"):
        if (timestring - int(file[:-4]))>=2:
            storage.child(path_on_cloud+ file).put(path_local+ file)
            storage.child(path_on_cloud+ file[:-4]+".jpeg").put(path_local+ file[:-4]+".jpeg")
            print("audio uploaded to firebase")	  
            print("image uploaded to firebase")
            timestr= datetime.now().strftime("%H:%M:%S")
            print(timestr)
            datestr=datetime.now().strftime("%d/%m/%Y")
            print(datestr)
#detail of data uploaded to firebase database
            data={
				'audio_file_name':file,
				  'date' : datestr,
				    'is_read_by_user':'false',
					  'time':timestr,
					    'image_captured':file[:-4]+".jpeg"	       	  
	             }

            print('data entered : ',data)
            result = ref.post('/All_devices/-MEMxh1nFvXai-nQqOZI/recorded_msgs/timestampp', data)
            print (result) 


        
 



