import cv2
import urllib.request

# Download haarcascade automatically
url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
urllib.request.urlretrieve(url, "haarcascade_frontalface_default.xml")

face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

def detect_faces(frame):
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.05,
        minNeighbors=4,
        minSize=(20,20)
    )

    return faces
