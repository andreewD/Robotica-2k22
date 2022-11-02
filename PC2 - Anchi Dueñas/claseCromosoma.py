import random
from clasePunto import *
class Cromosoma:    
    def __init__(self,Puntos,etiqueta):
        self.tamcromosoma = len(Puntos)
        self.Puntos = Puntos
        self.p = 0
        self.pA = 0
        self.fitness = 0
        self.etiqueta = 'C'+etiqueta
        self.Puntos = self.aleatorio(Puntos.copy())
           
    def aleatorio(self,Puntos):
        salida = []
        while len(Puntos)>0:
            i = random.randint(0,len(Puntos)-1)
            salida.append(Puntos[i])
            Puntos.pop(i)
        return salida
    def distancia(self):
        suma = 0
        for i in range(len(self.Puntos)-1):
            [x1,y1,_] = self.Puntos[i].P()
            [x2,y2,_] = self.Puntos[i+1].P()
            d = ((x2-x1)**2 + (y2-y1)**2)**0.5
            suma = suma + d
        return suma
        
    def mostrar(self):
        s = ""
        for i in range(len(self.Puntos)):
            s = s + "-" + self.Puntos[i].etiqueta
        s = str(self.etiqueta)+": "+str(round(self.distancia(),4)) + "\t" + str(round(self.fitness,4)) + "\t"+ str(round(self.p,4))+ "\t"+ str(round(self.pA,4)) + "\t" + s
        print(s)
