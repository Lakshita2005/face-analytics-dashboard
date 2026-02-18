import streamlit as st
import cv2
import pandas as pd
import numpy as np
import urllib.request
import time
from datetime import datetime

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="AI Face Analytics Dashboard",
    page_icon="👁️",
    layout="wide"
)

# ---------------- HEADER ----------------
st.title("👁️ Real-Time Face Analytics Dashboard")
st.markdown("""
This system performs **real-time face detection and analytics** using AI-powered computer vision.

It detects faces from live video, counts them, logs analytics, and generates reports.
""")

# ---------------- SIDEBAR ----------------
st.sidebar.title("System Control Panel")

run = st.sidebar.toggle("Start Camera")

st.sidebar.markdown("---")

st.sidebar.subheader("System Information")
st.sidebar.info("""
Backend: OpenCV Haar Cascade  
Frontend: Streamlit Dashboard  
Detection Type: Real-Time  
Analytics: Face Count + Time Logs  
""")

st.sidebar.markdown("---")

st.sidebar.subheader("About System")
st.sidebar.write("""
This AI system detects faces and generates analytics in real-time.

It can be used for:

• Smart surveillance  
• Crowd analytics  
• Office monitoring  
• Retail analytics  
• Security systems  
""")

# ---------------- MAIN LAYOUT ----------------
col1, col2, col3 = st.columns(3)

metric_faces = col1.empty()
metric_time = col2.empty()
metric_status = col3.empty()

# ---------------- VIDEO PLACEHOLDER ----------------
video_placeholder = st.empty()

# ---------------- ANALYTICS DATA ----------------
data = []
df = pd.DataFrame(columns=["Time", "Faces"])

# ---------------- LOAD CASCADE ----------------
url = "https://raw.githubusercontent.com/opencv/opencv/master/data/haarcascades/haarcascade_frontalface_default.xml"
urllib.request.urlretrieve(url, "face.xml")

face_cascade = cv2.CascadeClassifier("face.xml")

# ---------------- CAMERA ----------------
camera = cv2.VideoCapture(0)

# ---------------- SYSTEM DESCRIPTION ----------------
with st.expander("How This System Works"):
    st.write("""
    Step 1: Capture video from webcam  
    Step 2: Convert frame to grayscale  
    Step 3: Apply Haar Cascade detection  
    Step 4: Count detected faces  
    Step 5: Log analytics data  
    Step 6: Display dashboard insights  
    """)

with st.expander("Backend Architecture"):
    st.write("""
    Camera → OpenCV → Haar Cascade Model → Detection → Analytics Engine → Streamlit Dashboard
    """)

with st.expander("Detection Model Info"):
    st.write("""
    Model Type: Haar Cascade Classifier  
    Algorithm: Viola-Jones  
    Speed: Real-Time  
    Accuracy: High for frontal faces  
    """)

# ---------------- MAIN LOOP ----------------
while run:

    ret, frame = camera.read()

    if not ret:
        st.error("Camera not working")
        break

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = face_cascade.detectMultiScale(
        gray,
        scaleFactor=1.3,
        minNeighbors=5
    )

    face_count = len(faces)

    # Draw boxes
    for (x, y, w, h) in faces:
        cv2.rectangle(
            frame,
            (x, y),
            (x+w, y+h),
            (0, 255, 0),
            2
        )

    # Update metrics
    metric_faces.metric("Faces Detected", face_count)
    metric_time.metric("Current Time", datetime.now().strftime("%H:%M:%S"))
    metric_status.metric("System Status", "Running")

    # Log data
    now = datetime.now().strftime("%H:%M:%S")
    data.append({"Time": now, "Faces": face_count})

    df = pd.DataFrame(data)

    # Show video
    video_placeholder.image(frame, channels="BGR")

    # Show graph
    st.subheader("Face Detection Analytics")

    if len(df) > 1:
        st.line_chart(df.set_index("Time"))

    time.sleep(0.03)

# ---------------- STOP STATUS ----------------
if not run:
    metric_status.metric("System Status", "Stopped")

camera.release()

# ---------------- REPORT SECTION ----------------
st.markdown("---")
st.subheader("Analytics Report")

if not df.empty:

    st.dataframe(df)

    csv = df.to_csv(index=False)

    st.download_button(
        "Download Report",
        csv,
        file_name="face_analytics.csv",
        mime="text/csv",
        key="download1"
    )

# ---------------- FOOTER ----------------
st.markdown("---")

st.markdown("""
### System Capabilities

✔ Real-time face detection  
✔ Live analytics dashboard  
✔ Face count monitoring  
✔ Automated logging  
✔ Report generation  

This is a complete AI-powered analytics system.
""")
