import numpy as np
from PIL import Image
n,m = 0,0
def identidad(P):
    Q = P
    return Q
def inverso(P):
    Q = 255-P
    return Q
def binarizar(P,u):
    Q = (P>=u).astype(int)
    return Q
def filtrar3x3(I,M):
    Q = np.zeros((m,n))
    for i in range(1,m-1):
        for j in range(1,n-1):
            P = I[i-1:i+2,j-1:j+2]
            Q[i,j] = (P*M).sum()
    return Q
def resaltarborde(I,Mh,Mv):
    Q = np.zeros((m,n))
    for i in range(1,m-1):
        for j in range(1,n-1):
            P = I[i-1:i+2,j-1:j+2]
            Gx = (P*Mh).sum()
            Gy = (P*Mv).sum()
            Q[i,j] = (Gx**2 + Gy**2)**0.5
    return Q 
    
imgGray = Image.open("esferas.jpg").convert("L")
imgGray.show()
n,m = imgGray.size
imgNP = np.array(imgGray)
Promedio = (1.0/9.0)*np.ones((3,3))
Gaussiana = [[1.0/16.0,2.0/16.0,1.0/16.0],
             [2.0/16.0,4.0/16.0,2.0/16.0],
             [1.0/16.0,2.0/16.0,1.0/16.0]]
prewittH = [[1.0,0.0,-1.0],
            [1.0,0.0,-1.0],
            [1.0,0.0,-1.0]]

prewittV = [[-1.0,-1.0,-1.0],
            [0.0,0.0,0.0],
            [1.0,1.0,1.0]]
sobelH =   [[1.0,0.0,-1.0],
            [2.0,0.0,-2.0],
            [1.0,0.0,-1.0]]

sobelV =  [[-1.0,-2.0,-1.0],
            [0.0,0.0,0.0],
            [1.0,2.0,1.0]]

robertH =   [[0.0,0.0,0.0],
            [0.0,1.0,0.0],
            [0.0,0.0,-1.0]]

robertV =  [[0.0,0.0,0.0],
            [0.0,0.0,-1.0],
            [0.0,1.0,0.0]]
#resultado = binarizar(imgNP,128)
#resultado = filtrar3x3(imgNP,Gaussiana)
resultado = resaltarborde(imgNP,robertH,robertV)
im = Image.fromarray(resultado)
im.show()
