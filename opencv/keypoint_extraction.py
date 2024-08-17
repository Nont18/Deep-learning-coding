#เปิดวิดีโอด้วย OpenCV
import cv2
import mediapipe as mp
import csv
import os

def write_landmarks_to_csv(landmarks, frame_number, file_name, csv_data):
    print(f"Landmark coordinates for frame {frame_number}:")
    for idx, landmark in enumerate(landmarks):
        print(f"{mp_pose.PoseLandmark(idx).name}: (x: {landmark.x}, y: {landmark.y}, z: {landmark.z})")
        csv_data.append([file_name, frame_number, mp_pose.PoseLandmark(idx).name, landmark.x, landmark.y, landmark.z])

video_path = 'opencv/image/กระท่อม.mp4'
output_csv = 'C:/Users/araya/Desktop/vscode/python coding/opencv/coor_test.csv'

# Extract the file name without extension
file_name = os.path.splitext(os.path.basename(video_path))[0]

# Initialize MediaPipe Pose and Drawing utilities
mp_pose = mp.solutions.pose
mp_drawing = mp.solutions.drawing_utils
pose = mp_pose.Pose()

# Open the video file
cap = cv2.VideoCapture(video_path)


cap = cv2.VideoCapture("opencv\image\กระท่อม.mp4")

frame_number = 0
csv_data = []
while(cap.isOpened()):
    check, frame = cap.read() #รับภาพจากกล้องframe ต่อ frame
    if check == True:
        cv2.imshow("Output",frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

    if not check:
        break

    # Convert the frame to RGB
    frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)

    # Process the frame with MediaPipe Pose
    result = pose.process(frame_rgb)

    # Draw the pose landmarks on the frame
    if result.pose_landmarks:
        mp_drawing.draw_landmarks(frame, result.pose_landmarks, mp_pose.POSE_CONNECTIONS)

        # Add the landmark coordinates to the list and print them
        write_landmarks_to_csv(result.pose_landmarks.landmark, frame_number, file_name, csv_data)

    # Display the frame
    cv2.imshow('MediaPipe Pose', frame)

    # Exit if 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

    frame_number += 1

cap.release()
cv2.destroyAllWindows()

# Save the CSV data to a file
with open(output_csv, mode='a', newline='') as csvfile:
    csv_writer = csv.writer(csvfile)
    csv_writer.writerow(['file_name', 'frame_number', 'landmark', 'x', 'y', 'z'])
    csv_writer.writerows(csv_data)

cap.release()
cv2.destroyAllWindows()
