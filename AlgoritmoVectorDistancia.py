# -*- coding: cp1252 -*-
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

import lib.markup
import webbrowser
import os

class Nodo:
    distancias = []
    desde = []

#Algoritmo vector distancia
def auxVectDist(A):
    n = len(A)
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
    return nodos

#Despliegue en páginas de los resultados del algoritmo
def vectorDistancia(A, Acomp, lista_nodos, archivo, titulo):
    n = len(A)
    comparar = (n == len(Acomp))
    
    #Inicializar generador HTML
    page = lib.markup.page()
    page.init(title="Resultados", css="../css/style.css")
    page.h1(titulo)
    

    nodos = auxVectDist(A)
    if(comparar):
        nodos2 = auxVectDist(Acomp)
    else:
        nodos2 = nodos
                        
    page.table()
    page.tr()
    page.th("Nodo")

    for i in lista_nodos:
        page.th("Costo "+i)
    
    page.tr.close()

    for i in range (0, n):
        page.tr()
        page.td(lista_nodos[i])
        for j in range (0, n):
            if(comparar and nodos[i].distancias[j] != nodos2[i].distancias[j]):
                page.td(nodos[i].distancias[j], class_="dst")
            else:
                page.td(nodos[i].distancias[j])
        page.tr.close()
        

    page.table.close()
    if(comparar):
        page.p("(Costos modificados destacados)")

    file = open("results/"+archivo+".html", "w")
    file.write(str(page))
    file.close

    abspath = os.path.abspath("results/"+archivo+".html")
    webbrowser.open(abspath,2)
        



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


terminales = ["PC", "Router A", "Router B", "Router C", "Router D", "Router E", "Router F", "Router G", "Router H", "Router I", "Servidor"]

vectorDistancia(A,[], terminales, "inicial", "Costos involucrados a cada nodo")

A2 = [[0, 3, inf, inf, inf, inf, inf, inf, inf, inf, inf],
     [3, 0, 1, inf, inf, inf, inf, 4, inf, 10, inf],
     [inf, 1, 0, 9, inf, 8, inf, inf, inf, inf, inf],
     [inf, inf, 9, 0, 2, inf, inf, inf, inf, inf, inf],
     [inf, inf, inf, 2, 0, 9, 4, inf, inf, 2, inf],
     [inf, inf, 8, inf, 9, 0, 2, inf, inf, 1, inf],
     [inf, inf, inf, inf, 4, 2, 0, inf, 6, inf, inf],
     [inf, 4, inf, inf, inf, inf, inf, 0, 7, inf, inf],
     [inf, inf, inf, inf, inf, inf, 6, 7, 0, inf, inf],
     [inf, 10, inf, inf, 2, 1, inf, inf, inf, 0, 1],
     [inf, inf, inf, inf, inf, inf, inf, inf, inf, 1, 0]]


vectorDistancia(A2, A, terminales, "corteHI", "Costos involucrados a cada nodo al cortar enlace H-I")
