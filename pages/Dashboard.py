import streamlit as st
import cv2
import pandas as pd
import time
import os

from detector import detect_faces
from logger import log_data

# Header
st.markdown("""
# Live Face Monitoring System
Real-time AI-powered face analytics
""")

# Status bar
status_col1, status_col2 = st.columns([1,4])

start = status_col1.toggle("Start Camera")

status_col2.markdown(
    "<h4 style='color:lightgreen;'>System Status: RUNNING</h4>" if start else
    "<h4 style='color:red;'>System Status: STOPPED</h4>",
    unsafe_allow_html=True
)

st.divider()

# Layout
col1, col2 = st.columns([3,1])

video_placeholder = col1.empty()

# Metrics container
metric_container = col2.container()

current_metric = metric_container.empty()
peak_metric = metric_container.empty()
avg_metric = metric_container.empty()

cap = cv2.VideoCapture(0)

peak_count = 0

while start:

    ret, frame = cap.read()

    if not ret:
        st.error("Camera not accessible")
        break

    faces = detect_faces(frame)

    count = len(faces)

    if count > peak_count:
        peak_count = count

    log_data(count)

    # Draw boxes
    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)

    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    video_placeholder.image(
        frame,
        caption="Live Camera Feed",
        use_container_width=True
    )

    if os.path.exists("data_log.csv"):

        df = pd.read_csv("data_log.csv")

        avg = int(df["Face Count"].mean())

        current_metric.metric(
            "Current Faces",
            count,
            delta=None
        )

        peak_metric.metric(
            "Peak Faces",
            peak_count
        )

        avg_metric.metric(
            "Average Faces",
            avg
        )

    time.sleep(0.1)

cap.release()
