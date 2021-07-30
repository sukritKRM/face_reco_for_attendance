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
