import cv2
# video_path = "C:/Users/araya/Desktop/keypoints/video_extract/" + "อยาก.mp4"
# video_path = "C:/Users/araya/Downloads/WLASL2000/WLASL2000/64297.mp4"
video_path = "C:/Users/araya/Desktop/dataset-today/กระโปรง.mp4"

# class_name = os.path.splitext(os.path.basename(video_path))[0]
        
cap = cv2.VideoCapture(video_path)
success,image = cap.read()
count = 0
print(success)
while success:
  cv2.imwrite("important_frame_%d.jpg" % count, image)     # save frame as JPEG file      
  success,image = cap.read()
  print('Read a new frame: ', success)
  count += 1

