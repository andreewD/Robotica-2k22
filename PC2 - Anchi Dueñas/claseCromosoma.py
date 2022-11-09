import random
from clasePunto import *


class Cromosoma:
    def __init__(self, Puntos, etiqueta, inicial):
        self.tamcromosoma = len(Puntos)
        self.Puntos = Puntos
        self.p = 0
        self.pA = 0
        self.fitness = 0
        self.etiqueta = 'C'+etiqueta
        self.Puntos = self.aleatorio(Puntos.copy(), inicial)

    def line(self, point1, p2):
        A = (point1[1] - p2[1])  # type: ignore
        B = (p2[0] - point1[0])  # type: ignore
        C = (point1[0]*p2[1] - p2[0]*point1[1])  # type: ignore
        return A, B, -C

    def intersection(self, L1, L2):
        D = L1[0] * L2[1] - L1[1] * L2[0]
        Dx = L1[2] * L2[1] - L1[1] * L2[2]
        Dy = L1[0] * L2[2] - L1[2] * L2[0]
        if D != 0:
            x = Dx / D
            y = Dy / D
            # print('Intersection at', x, y)
            return True
        else:
            return False

    def aleatorio(self, Puntos, inicial):
        salida = []
        initialPoint = Puntos[inicial]
        del Puntos[inicial]

        while len(Puntos) > 0:
            i = random.randint(0, len(Puntos)-1)
            salida.append(Puntos[i])
            Puntos.pop(i)

        temp = [initialPoint, *salida]
        # Generate lines from consequent points
        lines = []
        for i in range(len(temp)-1):
            lines.append(self.line(temp[i].P(), temp[i+1].P()))
        # Check if lines intersect
        print('--------------------------------')
        for i in range(len(lines)-1):
            for j in range(i, len(lines)):
                if (self.intersection(lines[i], lines[j]) == False):
                    print('NO INTERSECTION')
                    print('Candidato',[initialPoint, *salida])
                else :
                    print('INTERSECTION')
                    print('Camino no válido')
        print('--------------------------------')
        return [initialPoint, *salida]

    def distancia(self):
        suma = 0
        for i in range(len(self.Puntos)-1):
            [x1, y1, _] = self.Puntos[i].P()
            [x2, y2, _] = self.Puntos[i+1].P()
            d = ((x2-x1)**2 + (y2-y1)**2)**0.5
            suma = suma + d
        return suma

    def mostrar(self):
        s = ""
        for i in range(len(self.Puntos)):
            s = s + "-" + self.Puntos[i].etiqueta
        s = str(self.etiqueta)+": "+str(round(self.distancia(), 4)) + "\t" + str(round(self.fitness, 4)
                                                                                 ) + "\t" + str(round(self.p, 4)) + "\t" + str(round(self.pA, 4)) + "\t" + s
        print(s)
