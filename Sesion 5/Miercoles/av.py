from claseCromosoma import *
import numpy as np
p0 = Punto(0,0,'P0')
p1 = Punto(100,0,'P1')
p2 = Punto(100,100,'P2')
p3 = Punto(70,70,'P3')
p4 = Punto(170,710,'P4')
p5 = Punto(10,80,'P5')
p6 = Punto(20,40,'P6')
global Ptos
global Pc
global Pm
Ptos = [p0,p1,p2,p3,p4,p5,p6]
tampoblacion = 4
Pc = 0.95
Pm = 0.2
tamgeneraciones = 10
def crearpoblacion(tampoblacion):
    pobla = []
    for i in range(tampoblacion):
        pobla.append(Cromosoma(Ptos,str(i)))
    return pobla
def mostrarpoblacion(P):
    print()
    for i in range(len(P)):
        P[i].mostrar()

def ordenarporfitness(P):
    for i in range(len(P)-1):
        for j in range(i+1,len(P)):
            if P[i].distancia()<P[j].distancia():
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
        if P[i].pA>=(aleatorio + 0.1):
            return P[i]
    return P[len(P)-1]
        
def seleccion(P):
    P1 = sacarpadre(P)
    P2 = sacarpadre(P)
    while P1.etiqueta==P2.etiqueta:
        P2 = sacarpadre(P)
    return P1,P2
def corregir(H):# [P2,P3,P1,P2,P4,P3] falta [P0,P5]
    Ps = Ptos.copy()
    for i in range(len(H.Puntos)):
        k = 0
        while k<len(Ps):
            if Ps[k].etiqueta==H.Puntos[i].etiqueta:
                Ps.pop(k)
            else:
                k = k + 1
    for i in range(len(H.Puntos)-1):
        for j in range(i+1,len(H.Puntos)):
            if H.Puntos[i].etiqueta==H.Puntos[j].etiqueta:
                H.Puntos[i] = Ps[0]
                Ps.pop(0)
    return H   
    
def cruce1punto(P1,P2):
    H1 = Cromosoma(Ptos,str(0))
    H2 = Cromosoma(Ptos,str(0))
    for i in range(len(P1.Puntos)):
        H1.Puntos[i] = P1.Puntos[i]
        H2.Puntos[i] = P2.Puntos[i]
    aleatorio = random.random()
    if aleatorio<Pc:
        punto = random.randint(2,len(P1.Puntos)-1)
        for i in range(punto,len(P2.Puntos)):
            H1.Puntos[i] = P2.Puntos[i]
            H2.Puntos[i] = P1.Puntos[i]
    H1 = corregir(H1)
    H2 = corregir(H2)
    return H1,H2
def mutacion(H):
    aleatorio = random.random()
    if aleatorio<Pm:
        punto1 = random.randint(1,len(H.Puntos)-1)
        punto2 = punto1
        while punto1==punto2:
            punto2 = random.randint(1,len(H.Puntos)-1)
        ptemp = H.Puntos[punto1]
        H.Puntos[punto1] = H.Puntos[punto2]
        H.Puntos[punto2] = ptemp
    return H
print("--- Inicia el proceso evolutivo ----------")
Poblacion = crearpoblacion(tampoblacion)
Poblacion = ordenarporfitness(Poblacion.copy())
Poblacion = calcularprobabilidadA(Poblacion)
mostrarpoblacion(Poblacion)
PoblacionT = crearpoblacion(tampoblacion)
for t in range(tamgeneraciones):
    for i in range(int(tampoblacion/2)):
        P1,P2 = seleccion(Poblacion.copy())
        H1,H2 = cruce1punto(P1,P2)
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

for p in Poblacion[len(Poblacion)-1].Puntos:
    print(p.P())