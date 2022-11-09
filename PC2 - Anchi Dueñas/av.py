from scipy.special import comb
from claseCromosoma import *
import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('esferas2.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

rojo_bajo1 = np.array([0, 100, 20])
rojo_alto1 = np.array([8, 255, 255])
rojo_bajo2 = np.array([175, 100, 20])
rojo_alto2 = np.array([179, 255, 255])
mascara_rojo1 = cv2.inRange(hsv, rojo_bajo1, rojo_alto1)
mascara_rojo2 = cv2.inRange(hsv, rojo_bajo2, rojo_alto2)
mascara_rojoUnido = cv2.add(mascara_rojo1, mascara_rojo2)
mascara_visualizado = cv2.bitwise_and(image, image, mask=mascara_rojoUnido)
cnts, _ = cv2.findContours(
    mascara_rojoUnido, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

positions = []
for c in cnts:
    epsilon = 0.01*cv2.arcLength(c, True)
    approx = cv2.approxPolyDP(c, epsilon, True)
    if len(approx) > 10:
        x, y, w, h = cv2.boundingRect(approx)
        positions.append([x, y])
        # Print the last point saved
        print('Point',len(positions)-1,'=>',positions[-1])
        cv2.putText(image, "("+str(x)+","+str(y)+")",
                    (x, y-5), 1, 1, (0, 0, 0), 1)
cv2.imshow('imagen', image)
cv2.imwrite('esferasRojas.jpg', image)
cv2.waitKey()
cv2.destroyAllWindows()


global Ptos
Ptos = []

for arr_i, arr in enumerate(positions):
    Ptos.append(Punto(arr[0], arr[1], 'Punto'+str(arr_i)))

inicialLabel = input('Ingrese el numero del punto inicial:')
# print('Ptos, ', Ptos)
puntoInicial = Ptos[int(inicialLabel)]
print('pTO INICIAL',puntoInicial)
global Pc
global Pm

tampoblacion = 100
Pc = 0.95
Pm = 0.2
tamgeneraciones = 10


def crearpoblacion(tampoblacion,inicial):
    pobla = []
    for i in range(tampoblacion):
        pobla.append(Cromosoma(Ptos, str(i),inicial))
    return pobla


def mostrarpoblacion(P):
    print()
    for i in range(len(P)):
        P[i].mostrar()


def ordenarporfitness(P):
    for i in range(len(P)-1):
        for j in range(i+1, len(P)):
            if P[i].distancia() < P[j].distancia():
                ct = P[i]
                P[i] = P[j]
                P[j] = ct
    return P


def calcularprobabilidadA(P):
    suma = 0
    for i in range(len(P)):
        suma = suma + P[i].distancia()
    pT = [(suma - p.distancia()) for p in P]
    maxdistancia = max(pT)
    sumaT = 0
    for pt in pT:
        sumaT = sumaT + pt
    pA = 0
    for i in range(len(P)):
        probabilidad = pT[i]/sumaT
        P[i].p = probabilidad
        P[i].pA = pA + probabilidad
        P[i].fitness = 1 - pT[i]/(maxdistancia*len(pT))
        pA = pA + probabilidad
    return P


def sacarpadre(P):
    aleatorio = random.random()
    for i in range(len(P)):
        if P[i].pA >= (aleatorio + 0.1):
            return P[i]
    return P[len(P)-1]


def seleccion(P):
    P1 = sacarpadre(P)
    P2 = sacarpadre(P)
    while P1.etiqueta == P2.etiqueta:
        P2 = sacarpadre(P)
    return P1, P2


def corregir(H):
    Ps = Ptos.copy()
    for i in range(len(H.Puntos)):
        k = 0
        while k < len(Ps):
            if Ps[k].etiqueta == H.Puntos[i].etiqueta:
                Ps.pop(k)
            else:
                k = k + 1
    for i in range(len(H.Puntos)-1):
        for j in range(i+1, len(H.Puntos)):
            if H.Puntos[i].etiqueta == H.Puntos[j].etiqueta:
                H.Puntos[i] = Ps[0]
                Ps.pop(0)
    return H


def cruce1punto(P1, P2,inicial):
    H1 = Cromosoma(Ptos, str(0),inicial)
    H2 = Cromosoma(Ptos, str(0),inicial)
    for i in range(len(P1.Puntos)):
        H1.Puntos[i] = P1.Puntos[i]
        H2.Puntos[i] = P2.Puntos[i]
    aleatorio = random.random()
    if aleatorio < Pc:
        punto = random.randint(2, len(P1.Puntos)-1)
        for i in range(punto, len(P2.Puntos)):
            H1.Puntos[i] = P2.Puntos[i]
            H2.Puntos[i] = P1.Puntos[i]
    H1 = corregir(H1)
    H2 = corregir(H2)
    return H1, H2


def mutacion(H):
    aleatorio = random.random()
    if aleatorio < Pm:
        punto1 = random.randint(1, len(H.Puntos)-1)
        punto2 = punto1
        while punto1 == punto2:
            punto2 = random.randint(1, len(H.Puntos)-1)
        ptemp = H.Puntos[punto1]
        H.Puntos[punto1] = H.Puntos[punto2]
        H.Puntos[punto2] = ptemp
    return H


print("--- Inicia el proceso evolutivo ----------")
Poblacion = crearpoblacion(tampoblacion,int(inicialLabel))
Poblacion = ordenarporfitness(Poblacion.copy())
Poblacion = calcularprobabilidadA(Poblacion)
mostrarpoblacion(Poblacion)
PoblacionT = crearpoblacion(tampoblacion,int(inicialLabel))
for t in range(tamgeneraciones):
    for i in range(int(tampoblacion/2)):
        P1, P2 = seleccion(Poblacion.copy())
        H1, H2 = cruce1punto(P1, P2,int(inicialLabel))
        H1 = mutacion(H1)
        H2 = mutacion(H2)
        H1.etiqueta = 'C'+str(2*i)
        H2.etiqueta = 'C'+str(2*i+1)
        PoblacionT[2*i] = H1
        PoblacionT[2*i+1] = H2
    Poblacion = ordenarporfitness(PoblacionT)
    Poblacion = calcularprobabilidadA(Poblacion)
    print(str(t)+"---------------")
    mostrarpoblacion(Poblacion)
print("Mejor solucion")
Poblacion[len(Poblacion)-1].mostrar()

puntos_ordenados = []
label_puntos_ordenados = []
for p in Poblacion[len(Poblacion)-1].Puntos:
    label_puntos_ordenados.append(p.etiqueta)
    puntos_ordenados.append([p.P()[0], p.P()[1]])

print('Puntos ordenados:')
print(puntos_ordenados)

# Polinomio de Bernstein
def bernstein_poly(i, n, t):
    return comb(n, i) * (t**(n-i)) * (1 - t)**i

# Bezier
def bezier_curve(points, nTimes=1000):
    nPoints = len(points)
    xPoints = np.array([p[0] for p in points])
    yPoints = np.array([p[1] for p in points])

    t = np.linspace(0.0, 1.0, nTimes)

    polynomial_array = np.array(
        [bernstein_poly(i, nPoints-1, t) for i in range(0, nPoints)])

    xvals = np.dot(xPoints, polynomial_array)
    yvals = np.dot(yPoints, polynomial_array)

    return xvals, yvals


if __name__ == "__main__":
    nPoints = len(puntos_ordenados)+1
    # points = np.random.rand(nPoints, 2)*200
    xpoints = [p[0] for p in [*puntos_ordenados, puntos_ordenados[0]]]
    ypoints = [p[1] for p in [*puntos_ordenados, puntos_ordenados[0]]]

    xvals, yvals = bezier_curve(
        [*puntos_ordenados, puntos_ordenados[0]], nTimes=10000)
    plt.plot(xvals, yvals, 'r', linewidth=12)
    plt.plot(xpoints, ypoints, "ro")  # puntos de control
    plt.axis('off')  # quitar ejes
    for nr in range(len(puntos_ordenados)):
        plt.text(puntos_ordenados[nr][0], puntos_ordenados[nr]
                 [1], label_puntos_ordenados[nr])  # type: ignore
    plt.gca().invert_yaxis()
    plt.savefig('bezier_curve.png')

    plt.show()
