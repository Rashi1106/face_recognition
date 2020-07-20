
import face_recognition
import os
import cv2

video_capture = cv2.VideoCapture(0)

Known_Faces_Dir = "/home/rashi/vediobell/known_face"
Unknown_Faces_Dir = "/home/rashi/vediobell/unknown_face"

#image= cv2.imread(path)

known_face = []
known_names =[]

#print("processing known faces")     
for dirpath, dnames, fnames in os.walk("known_face"):
    for f in fnames:
        if f.endswith(".jpg") or f.endswith(".png"):
            image =face_recognition.load_image_file("known_face + "/" + fnames")
            encoding = face_recognition.face_encodings(image)[0]
            known_face.append(encoding)
            known_names.append(name)

#print("processing unknown faces")   
for dirpath, dnames, fnames in os.walk("unknown_face"):
    for f in fnames:
            print(fnames)
            frame =face_recognition.load_image_file("{unknown_face}/{fnames}")
            locations = face_recognition.face_locations(frame ,model ="cnn")
            
            encoding = face_recognition.face_encodings(frame,locations)
            frame = cv2.cvtColor(frame,cv2.Color_RGB2BGR)
        
            for face_encodings,face_locations in zip(encoding, locations):
                result = face_recognition.compare_faces(known_face, face_encodings,Tolerance= 0.6)
                match = None
                if True in result:
                    match = known_names[result.index(True)]
                    print("Match found: {match}")
                else:
                    print("Unknown")
                    
                top_left = (face_locations[3], face_locations[0])
                bottom_right = (face_locations[1], face_locations[2])
                cv2.rectangle(frame, top_left, bottom_right, (0, 255, 255), 2)  
                                                               #color  thickness /stroke                                                 
               
                top_left = (face_locations[3], face_locations[0])
                bottom_right = (face_locations[1], face_locations[2]+20)
                cv2.rectangle(frame, top_left, bottom_right, (0, 255, 255),cv2.FILLED)
                cv2.putText(frame, match , (face_locations[3]+10, face_locations[2]+15), cv2.FONT_HERSHEY_DUPLEX, 1.0, (0, 255, 0),1)

while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    cv2.imshow('Video', frame)
    key = cv2.waitKey(1)
    if key == ord('q'): #press Esc to quit
        break;

# When everything is done
video_capture.release()
cv2.destroyAllWindows()