import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import analisis_tecnico as at
import math
import regex
import re

plt.style.use("seaborn")

repl_list = {',': '.', '%': '', 'K': '000',}

df = pd.read_csv('copper_daily.csv', sep=',')
df.replace(repl_list, regex=True, inplace=True)
# print(df.head())

fecha = np.array(df['Date'])[::-1]
apertura = np.array(df['Open'])[::-1]
maximo = np.array(df['High'])[::-1]
minimo = np.array(df['Low'])[::-1]
cierre = np.array(df['Price'])[::-1]
variacion = cierre - apertura

#df1 = pd.DataFrame({'Fecha':fecha, 'Apertura':apertura, 'Cierre':cierre, 'Maximo':maximo, 'Minimo':minimo, 'variacion':variacion})
#df1.to_csv(r'Desktop\datos.csv', index=True)

maximo_global = np.amax(maximo)
minimo_global = np.amin(minimo)

var = (maximo_global - minimo_global) / 100
sesiones = 5

aperturas_clave_reducidas = at.aperturas_clave_reducidas(apertura, sesiones, var)
media_movil1=at.media_movil(apertura, 20)
media_movil2=at.media_movil(apertura, 200)

soportes_resistencias = np.zeros((len(aperturas_clave_reducidas), len(apertura)))

for i in range(len(aperturas_clave_reducidas)):
    for k in range(len(apertura)):
        soportes_resistencias[i, k] = aperturas_clave_reducidas[i]

plt.plot(fecha, apertura, 'black')
plt.plot(fecha, media_movil1, 'blue')
plt.plot(fecha, media_movil2, 'green')

for i in range(len(aperturas_clave_reducidas)):
    plt.plot(fecha, soportes_resistencias[i], 'red')

plt.show()


