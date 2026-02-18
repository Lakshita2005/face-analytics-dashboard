# Real-Time Face Analytics Dashboard

A professional AI-powered real-time face detection and analytics dashboard built using OpenCV and Streamlit.

This system detects human faces from live webcam feed and provides real-time analytics through an interactive multi-page dashboard.

---

## Features

- Real-time face detection
- Multi-page interactive dashboard
- Live face count monitoring
- Analytics and visualization
- Data logging system
- Downloadable reports
- Modular and scalable architecture

---

## Dashboard Pages

### Dashboard
- Live webcam feed
- Real-time face detection
- Face count display

### Analytics
- Face count graphs
- Time-based analytics
- Trend visualization

### Reports
- Downloadable CSV reports
- Historical data access

---

## Tech Stack

- Python
- OpenCV
- Streamlit
- NumPy
- Pandas

---

## Project Architecture

FACE_ANALYTICS_DASHBOARD/
│
├── app.py → Main application entry
├── detector.py → Face detection logic
├── logger.py → Data logging
│
├── pages/
│ ├── Dashboard.py
│ ├── Analytics.py
│ └── Reports.py
│
├── data/ → Stored analytics data
│
├── .streamlit/
│ └── config.toml → UI configuration
│
├── haarcascade_frontalface_default.xml → Face detection model
│
├── requirements.txt
│
└── README.md


---

## How It Works

1. Webcam captures live video
2. Frames processed using OpenCV
3. Haar Cascade detects faces
4. System counts faces
5. Data logged with timestamps
6. Dashboard displays analytics

---

## Installation

Clone repository:
git clone https://github.com/YOUR\_USERNAME/face-analytics-dashboard.git


1.Go to project folder:
cd face-analytics-dashboard

2.Install dependencies:
pip install -r requirements.txt

3.Run application:
streamlit run app.py


---

## Use Cases

- Smart surveillance systems
- Crowd monitoring
- Office attendance analytics
- Retail analytics
- Security monitoring

---

## Future Improvements

- Face recognition
- Database integration
- Cloud deployment
- Multi-camera support

---

## Author

Lakshita Bhardwaj

---

