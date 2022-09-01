#PARCIAL#3
#Raul Ricardo Reales Cohen
#Erick Enrique Bastidas Santana

#Primer punto
from scipy.stats import binom
data_binom = binom.rvs(n=10,p=0.8,size=1000)
print(data_binom)

for i in data_binom:
    M = data_binom[0]
    if i < M:
        M = i
print(M)
print("El valor minimo es:", M)

#Segundo Punto
import numpy as np
from statistics import mean,pstdev

indices = np.random.permutation(len(data_binom))
indices = indices[:100]
data_binom_nan = data_binom.copy().astype(np.double)
data_binom_nan[indices] = np.nan
print(data_binom_nan)

p = data_binom_nan[np.logical_not(np.isnan(data_binom_nan))]
mean(data_binom_nan)
promedio = mean(p)
desviacion = pstdev(p)
print(p)
print(promedio)
print(desviacion)
print(f"El promedio es: {promedio}, y la desviacion estandar {desviacion}")
