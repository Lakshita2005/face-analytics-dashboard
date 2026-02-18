import csv
import os
from datetime import datetime

file_path = "data_log.csv"

def log_data(face_count):

    file_exists = os.path.isfile(file_path)

    with open(file_path, "a", newline="") as f:

        writer = csv.writer(f)

        if not file_exists:
            writer.writerow(["Time", "Face Count"])

        writer.writerow([
            datetime.now().strftime("%H:%M:%S"),
            face_count
        ])
