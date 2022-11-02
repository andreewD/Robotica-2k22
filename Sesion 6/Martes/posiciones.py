import cv2
import numpy as np
image = cv2.imread('esferas2.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray,50,165)
color_blanco = np.array([255,255,255])
color_negro = np.array([0,0,0])

hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
mascara_unida = cv2.inRange(hsv,color_negro, color_blanco)
mascara_visualizado = cv2.bitwise_and(image,image,mask=mascara_unida)
cnts,_ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
positions = []
for c in cnts:
    epsilon = 0.01*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)
    if len(approx)>10:
        x,y,w,h = cv2.boundingRect(approx)
        print(x,y,w,h)
        positions.append([x,y])
        cv2.putText(image,"("+str(x)+","+str(y)+")",(x,y-5),1,1,(0,0,0),1)
cv2.imshow('imagen',image)
cv2.waitKey(10000)
cv2.destroyAllWindows()


