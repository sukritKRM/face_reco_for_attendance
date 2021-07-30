# ATTENDANCE SHEET MAKER
The problem is the time wasted by the teacher every morning and every end of the period to check the no. of the children present in the class.

## PROPOSED SOLUTION
A system that will recognize the faces of children present by facial recognition and make a list of students by the names corresponding to the images of their faces

## Instructions to download shape predictor face landmarks
To download the shape predictor face landmarks, click <a href="https://drive.google.com/drive/folders/1XpA2wKfutscRGtWhQ-cUxYsTatOH7ihl?usp=sharing">here</a>.

## Database Structure
```
database
   |
   |-----my_db
   |       |
   |       |------A(name)
   |       |      |--------A.jpg
   |       |------B(name)
   |       |      |--------B.jpg

```
## PIPELINE

- [X] Create a dummy database
- [X] computing the eye aspect ratio
- [X] Defining the threshold of the Eye_aspect_ratio(ear) below which we assume that the eye is closed
- [X] Defining the minimal number of consecutive frames with a low enough ear value for a blink to be detected
- [X] Using argparse for getting arguments from command line
- [X] initialising dlib's face detector (HOG-based) and facial landmark predictor
- [X] Choosing indices for the left and right eye
- [X] Starting the video stream
- [X] Looping over the frames of video stream: grabbing the frame, resizing it, converting it to grayscale and detecting faces in the grayscale frame
- [X] Looping over the face detections: determining the facial landmarks, converting the facial landmark (x, y)-coordinates to a numpy arrays, extracting the left and right eye coordinates, and using them to compute the average eye aspect ratio for both eyes
- [X] If the eye aspect ratio is below the threshold, increment counter, if the eyes are closed longer than for 2 secs, raise an alert
- [X] Performing the facial recognition using deepface and extracting the required name from the pandas dataframe
- [X] Writing the extracted name to a csv file 

## QUICK START
- Cloning the Repository: 

        git clone https://github.com/sukritKRM/face_reco_for_attendance
        
- Entering the directory: 

        cd face_reco_for_attendance
        
- Setting up the Python Environment with dependencies:

        pip install -r requirements.txt
       
- Running the file 

        python ./detect.py --shape-predictor shape_predictor_68_face_landmarks.dat     

<HR>
   THIS PROJECT HAS BEEN DEVOLOPED BY <a href="https://github.com/sukritKRM">SUKRIT</a>
   
   

