#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pickle
import numpy as np
import pandas as pd 
import math as m

with open('matriz_valores.pkl', 'rb') as archivo: 
    matriz= pickle.load(archivo)


df = pd.DataFrame(matriz)

# Ruta del archivo CSV donde se guardará el DataFrame
ruta_archivo_csv = 'matriz_guardada.csv'

# Guardar el DataFrame en el archivo CSV sin incluir índices y encabezados
df.to_csv(ruta_archivo_csv, index=False, header=False)

print(matriz[46])