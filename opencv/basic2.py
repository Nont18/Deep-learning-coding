#แสดงผลภาพ
import cv2
img = cv2.imread("opencv/image/cat.jpg")

cv2.imshow("Output",img)
# cv2.waitKey(delay=5000)
cv2.waitKey(0)
cv2.destroyAllWindows()