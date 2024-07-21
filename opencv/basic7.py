#เปิดวิดีโอด้วย OpenCV
import cv2

cap = cv2.VideoCapture("opencv\image\Video.mp4")

while(cap.isOpened()):
    check, frame = cap.read() #รับภาพจากกล้องframe ต่อ frame
    if check == True:
        cv2.imshow("Output",frame)
        if cv2.waitKey(1) & 0xFF == ord("e"):
            break
    else:
        break

cap.release()
cv2.destroyAllWindows()
