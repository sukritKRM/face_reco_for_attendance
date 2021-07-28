from typing import Counter
from deepface import DeepFace
import dlib
import imutils
from numpy.core.numeric import identity
from scipy.spatial import distance as dist
import cv2
from imutils.video import FileVideoStream, VideoStream
from imutils import face_utils
import argparse
import pandas as pd
import os
import time
import numpy as np
import csv



def eye_aspect_ratio(eye):
    vertical_dist=dist.euclidean(eye[1],eye[5])+dist.euclidean(eye[2],eye[4])
    horisontal_dist=dist.euclidean(eye[0],eye[3])
    ear=vertical_dist/(horisontal_dist*2.0)
    return ear

blink_threshold=0.19
consec_frame_number=2

ap=argparse.ArgumentParser(description=' eye blink detection ')
ap.add_argument("-p","--shape-predictor",required=True,help="path to facial landmark predictor")
args=vars(ap.parse_args())
print("loading facial landmark predictor")
detector=dlib.get_frontal_face_detector()
predictor=dlib.shape_predictor(args["shape_predictor"])

(left_s,left_e)=face_utils.FACIAL_LANDMARKS_IDXS["left_eye"]
(right_s,right_e)=face_utils.FACIAL_LANDMARKS_IDXS["right_eye"]


vs=VideoStream(src=0).start()
print("staring stream from builtin camera")
fileStream=False

counter=0
total=0
alert=False
start_time=0
frame=vs.read()
filename='img.jpg'

while(not fileStream) or (frame is not None):
    frame=imutils.resize(frame,width = 640)
    gray_frame=cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    rects=detector(gray_frame,0)
    ear=0
    for rect in rects:
        shape=predictor(gray_frame,rect)
        shape=face_utils.shape_to_np(shape)
        left_eye=shape[left_s:left_e]
        right_eye=shape[right_s:right_e]
        left_ear=eye_aspect_ratio(left_eye)
        right_ear=eye_aspect_ratio(right_eye)
        ear=(left_ear+right_ear)/2.0

        left_eye_hull=cv2.convexHull(left_eye)
        right_eye_hull=cv2.convexHull(right_eye)

        cv2.drawContours(frame,[left_eye_hull],-1,(0,0,255),1)
        cv2.drawContours(frame,[right_eye_hull],-1,(0,0,255),1)

        if ear < blink_threshold:
            counter+=1
            if start_time==0:
                start_time=time.time()
            else:
                end_time=time.time()
                if end_time-start_time>2:
                    alert=True
        else:
            if counter>=consec_frame_number:
                total+=1
            counter=0
            start_time=0
            alert=False
    if alert:
        cv2.putText(frame,"ALERT!!!",(150,30),cv2.FONT_HERSHEY_COMPLEX,0.7,(0,0,255),2)
    
    cv2.imshow("frame",frame)
    key=cv2.waitKey(1) & 0xFF
    if total>=1:
        cv2.imwrite(filename,frame)
        df=DeepFace.find(img_path="img.jpg",db_path="database/my_db")
        if df.empty:
            print("no match")
        else:
            names=[]
            string= df["identity"][0]
            path= os.path.dirname(string)
            name= os.path.basename(path)
            print("identified as: ",name)
            names.append(name)
            with open('attendance_sheet.csv','a',encoding='UTF8') as file:
                writer=csv.writer(file)
                writer.writerow(names)
                file.close()
        time.sleep(2)
        break
    if key==ord('q'):
        break
    frame= vs.read()

cv2.destroyAllWindows()
vs.stop()

            

