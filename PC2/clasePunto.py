import numpy as np
import math
class Punto:
    def __init__(self,x,y,etiqueta):
        self.x = x
        self.y = y
        self.etiqueta = etiqueta
    def P(self):
        return np.array([self.x,self.y,1])
    def T(self,Tx,Ty):        
        Tr = np.array([[1,0,0],
                     [0,1,0],
                     [Tx,Ty,0]])
        Pr = np.dot(self.P(),Tr)
        return Punto(Pr[0],Pr[1])  # type: ignore
    def R(self,a):
        a = a*math.pi/180
        Rot = np.array([[math.cos(a),math.sin(a),0],
             [-math.sin(a),math.cos(a),0],
             [0,0,1]])
        Pr = np.dot(self.P(),Rot)
        return Punto(Pr[0],Pr[1])  # type: ignore
    def ejeX(self):
        RefX = np.array([[1,0,0],
                         [0,-1,0],
                         [0,0,1]])
        Pr = np.dot(self.P(),RefX)
        return Punto(Pr[0],Pr[1])  # type: ignore
    def ejeY(self):
        RefY = np.array([[-1,0,0],
                         [0,1,0],
                         [0,0,1]])
        Pr = np.dot(self.P(),RefY)
        return Punto(Pr[0],Pr[1])  # type: ignore
    def ejeD(self):
        RefD = np.array([[-1,0,0],
                         [0,-1,0],
                         [0,0,1]])
        Pr = np.dot(self.P(),RefD)
        return Punto(Pr[0],Pr[1])  # type: ignore
    
