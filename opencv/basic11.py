#วาดเส้นตรง
import cv2

#อ่านภาพ
img = cv2.imread("opencv\image\cat.jpg")

#กำหนดขนาด
imgresize = cv2.resize(img,(700,700))

#วาดสี่เหลี่ยม
# rectangle(ภาพ, มุมที่1 (บนซ้าย), มุมที่2 (ล่างขวา), สี, ความหนา )
cv2.rectangle(imgresize, (0,0), (100,200),(0,0,255),10)


cv2.imshow("Output",imgresize)
cv2.waitKey(0)
cv2.destroyAllWindows()