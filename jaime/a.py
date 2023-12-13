#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pickle
import numpy as np
import pandas as pd

with open('matriz_IK.pkl', 'rb') as archivo:
    matriz = pickle.load(archivo)


matriz=np.array(matriz)
print(matriz.shape)


# Redondear todos los primeros términos al tercer decimal
matriz[:, 0] = np.round(matriz[:, 0], decimals=3)*100
# Redondear todos los primeros términos al tercer decimal
matriz[:, 1] = np.round(matriz[:, 1], decimals=3)*100
np.set_printoptions(suppress=True)


# Identificar las filas que cumplen con la condición
condicion = (matriz[:, 0].astype(float) % 1.0 >= 0.2) & (matriz[:, 0].astype(float) % 1.0 <= 0.8)

# Eliminar las filas que cumplen con la condición
matriz = matriz[~condicion]

# Identificar las filas que cumplen con la condición
condicion = (matriz[:, 1].astype(float) % 1.0 >= 0.2) & (matriz[:, 1].astype(float) % 1.0 <= 0.8)

# Eliminar las filas que cumplen con la condición
matriz = matriz[~condicion]


matriz[:, 0] = np.round(matriz[:, 0], decimals=0)
matriz[:, 1] = np.round(matriz[:, 1], decimals=0)

elementos_unicos = np.unique(matriz[:,0])

matriz_2x2=np.zeros((50,137), dtype=object)
for i in range(50):
    for j in range(137):
        indices_filas = np.where((matriz[:, 0] == (i)) & (matriz[:, 1] == (j)))
        if len(indices_filas[0])!=0:
            posicion=indices_filas[0][0]
            matriz_2x2[i,j]=np.array(matriz[int(posicion)])
            


with open('matriz_IK_lista.pkl', 'wb') as archivo:
    pickle.dump(matriz_2x2, archivo)

# Ruta del archivo CSV donde se guardará el DataFrame
ruta_archivo_csv = 'matriz_guardada.csv'

df = pd.DataFrame(matriz_2x2)

# Guardar el DataFrame en el archivo CSV sin incluir índices y encabezados
df.to_csv(ruta_archivo_csv, index=False, header=False)

