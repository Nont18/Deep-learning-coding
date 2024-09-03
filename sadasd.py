import sys
import cv2
import os
from sys import platform
import argparse
import csv

# Setup OpenPose paths
sys.path.append("C:/Users/araya/Desktop/openpose-master/build/python/openpose/Release")
import pyopenpose as op


# Flags
parser = argparse.ArgumentParser()
parser.add_argument("--image_path", default="C:/Users/araya/Desktop/openpose-master/examples/media/COCO_val2014_000000000192.jpg", help="Process an image. Read all standard formats (jpg, png, bmp, etc.).")
args = parser.parse_known_args()

# Initialize OpenPose
params = dict()
params["model_folder"] = "C:/Users/araya/Desktop/openpose-master/models"
opWrapper = op.WrapperPython()
opWrapper.configure(params)
opWrapper.start()

# Open video file
cap = cv2.VideoCapture("C:/Users/araya/Desktop/vscode/Deep-learning-coding/opencv/image/dataset/กฎกระทรวง.mp4")

# Initialize CSV file outside the loop
with open('keypoints.csv', mode='w', newline='') as file:
    writer = csv.writer(file)
    
    # Prepare an aggregated list of keypoints for the entire video
    aggregated_keypoints = []

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        # Prepare the frame for OpenPose
        datum = op.Datum()
        datum.cvInputData = frame
        opWrapper.emplaceAndPop(op.VectorDatum([datum]))

        # Extract keypoints
        pose_keypoints = datum.poseKeypoints

        # Aggregate keypoints
        if pose_keypoints is not None and len(pose_keypoints) > 0:
            for person in pose_keypoints:
                for keypoint in person:
                    aggregated_keypoints.extend([keypoint[0], keypoint[1], keypoint[2]])  # x, y, confidence

    # Write the aggregated keypoints as a single row to the CSV file
    writer.writerow(aggregated_keypoints)

cap.release()
