#ปรับเปลี่ยนขนาดภาพ
import cv2
img = cv2.imread("opencv/image/cat.jpg",0) #เปลี่ยนเป็นขาว-ดำ
imgresize = cv2.resize(img,(400,400))

#แสดงภาพ
cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()
