import cv2
import numpy as np
image = cv2.imread('esferas.jpg')
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
canny = cv2.Canny(gray,10,150)
cv2.imshow('tono gris',gray)
#cv2.imshow('Canny',canny)
azul_bajo = np.array([110,50,50])
azul_alto = np.array([130,255,255])

rojo_bajo = np.array([175,100,20])
rojo_alto = np.array([179,255,255])

hsv = cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
mascara_azul = cv2.inRange(hsv,azul_bajo,azul_alto)
mascara_rojo = cv2.inRange(hsv,rojo_bajo,rojo_alto)
#cv2.imshow('mascaraazul',mascara_azul)
cv2.imshow('mascararojo',mascara_rojo)

rojo_bajo1 = np.array([0,100,20])
rojo_alto1 = np.array([8,255,255])
rojo_bajo2 = np.array([175,100,20])
rojo_alto2 = np.array([179,255,255])
mascara_rojo1 = cv2.inRange(hsv,rojo_bajo1,rojo_alto1)
mascara_rojo2 = cv2.inRange(hsv,rojo_bajo2,rojo_alto2)
mascara_rojoUnido = cv2.add(mascara_rojo1,mascara_rojo2)
mascara_visualizado = cv2.bitwise_and(image,image,mask=mascara_rojoUnido)
cv2.imshow('mascarasolorojo',mascara_visualizado)
#cnts,_ = cv2.findContours(canny,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
cnts,_ = cv2.findContours(mascara_rojoUnido,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
for c in cnts:
    epsilon = 0.01*cv2.arcLength(c,True)
    approx = cv2.approxPolyDP(c,epsilon,True)
    if len(approx)>10:
        x,y,w,h = cv2.boundingRect(approx)
        print(x,y,w,h)
        cv2.putText(image,"("+str(x)+","+str(y)+")",(x,y-5),1,1,(0,0,0),1)
cv2.imshow('imagen',image)
