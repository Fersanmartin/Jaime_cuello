#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import numpy as np
import pandas as pd 
import math as m

with open('matriz_IK_lista.pkl', 'rb') as archivo: 
    matriz= pickle.load(archivo)

mat1=[[82,0],[76,-5800],[70,-11700],[65,-16700],[60,-21400],[55,-26400],[50,-32000]]
mat2=[[45,0], [40,-600],[35,-1600],[30,-3300],[25,-5000],[20,-6200],[15,-7800],[10,-9200],[5,-10400],[0,-14400]]

for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        if type(matriz[i,j]) != int :
            #print(matriz[i,j])
            for k in range(3):
                ma=matriz[i,j]
                matriz[i,j][2+k]= (ma[int(2+k)]*180)/m.pi
                

def encontrar_indices_mas_cercanos(matriz, valor):
    diferencias = [(abs(valor - elem[0]), i) for i, elem in enumerate(matriz)]
    diferencias.sort()

    indice1 = diferencias[0][1]
    indice2 = diferencias[1][1]

    return indice1, indice2

def aproximacion_lineal(punto1, punto2, valor_x):
    x1, y1 = punto1
    x2, y2 = punto2

    # Calcular la pendiente (m) y la ordenada al origen (b)
    m = (y2 - y1) / (x2 - x1)
    b = y1 - m * x1

    # Calcular el valor correspondiente a la aproximación lineal
    valor_y = m * valor_x + b

    return valor_y

for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        x,y= [i,j]
        lista=matriz[x,y]
        if type(lista) != int:
            angulo1=82-lista[2]
            angulo2=45-lista[3]
            # Obtener los dos puntos más cercanos
            indice1, indice2 = encontrar_indices_mas_cercanos(mat1, angulo1)
            punto1 = mat1[indice1]
            punto2 = mat1[indice2]
            # Realizar la aproximación lineal para obtener el valor correspondiente al segundo elemento
            valor_1_aproximado = aproximacion_lineal(punto1, punto2, angulo1)

            # Obtener los dos puntos más cercanos
            indice1, indice2 = encontrar_indices_mas_cercanos(mat2, angulo2)
            punto1 = mat2[indice1]
            punto2 = mat2[indice2]
            # Realizar la aproximación lineal para obtener el valor correspondiente al segundo elemento
            valor_2_aproximado = aproximacion_lineal(punto1, punto2, angulo2)
            

            matriz[i,j][2]=valor_1_aproximado
            matriz[i,j][3]=valor_2_aproximado

with open('matriz_valores.pkl', 'wb') as archivo:
    pickle.dump(matriz, archivo)