#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      SEBA
#
# Created:     16/06/2014
# Copyright:   (c) SEBA 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python

class Nodo:
    distancias = []
    desde = []

#A: Matriz de costos inicial; n: numero de routers
def vectorDistancia(A, n):

    nombreNodos = ['PC', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'Servidor']
    nodos = []
    for i in range(0, n):
        x = Nodo()
        x.distancias = [0] * n
        x.desde = [0] * n
        nodos.append(x)


    for i in range(0, n):
        for j in range(0, n):
            nodos[i].distancias[j] = A[i][j]
            nodos[i].desde[j] = j


    cuenta = 1

    while (cuenta != 0):
        cuenta = 0

        for i in range (0, n):
            for j in range (0, n):
                for k in range (0, n):
                    if nodos[i].distancias[j] > A[i][k] + nodos[k].distancias[j]:
                        nodos[i].distancias[j] = nodos[i].distancias[k] + nodos[k].distancias[j]
                        nodos[i].desde[j] = k
                        cuenta += 1

    for i in range (0, n):
        if (i == 0):
            print "Para PC"
        elif (i == n-1):
            print "Para el Servidor"
        else:
            print "Para el router", i+1
        for j in range (0, n):
            if (j+1 == 1):
                print "PC", "Costo:", nodos[i].distancias[j]
            elif (j+1 == n):
                print "Servidor", "Costo:", nodos[i].distancias[j]
            else:
                print "Router", j+1, "Costo:", nodos[i].distancias[j]
        print "\n"

inf = float("inf")

#Matriz de costos inicial para el problema planteado

A = [[0, 3, inf, inf, inf, inf, inf, inf, inf, inf, inf],
     [3, 0, 1, inf, inf, inf, inf, 4, inf, 10, inf],
     [inf, 1, 0, 9, inf, 8, inf, inf, inf, inf, inf],
     [inf, inf, 9, 0, 2, inf, inf, inf, inf, inf, inf],
     [inf, inf, inf, 2, 0, 9, 4, inf, inf, 2, inf],
     [inf, inf, 8, inf, 9, 0, 2, inf, inf, 1, inf],
     [inf, inf, inf, inf, 4, 2, 0, inf, 6, inf, inf],
     [inf, 4, inf, inf, inf, inf, inf, 0, 7, inf, inf],
     [inf, inf, inf, inf, inf, inf, 6, 7, 0, 3, inf],
     [inf, 10, inf, inf, 2, 1, inf, inf, 3, 0, 1],
     [inf, inf, inf, inf, inf, inf, inf, inf, inf, 1, 0]]

n = 11

print vectorDistancia(A, n)