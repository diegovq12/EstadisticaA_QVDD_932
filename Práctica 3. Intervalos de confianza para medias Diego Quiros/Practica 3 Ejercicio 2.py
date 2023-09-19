# -*- coding: utf-8 -*-
"""
@author: diego
Practica 3 Ejercicio 2
"""
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# Datos
media_muestral = 0.310  # Profundidad promedio de la muestra
desviacion_estandar = 0.0015  # Desviación estándar poblacional
tamano_muestra = 75
nivel_confianza = 0.95

# Calcular el intervalo de confianza
z = stats.norm.ppf((1 + nivel_confianza) / 2)
error_estandar = desviacion_estandar / np.sqrt(tamano_muestra)
intervalo_confianza = (media_muestral - z * error_estandar, media_muestral + z * error_estandar)

# Imprimir el intervalo de confianza
print(f"Intervalo de confianza del {nivel_confianza * 100}%: ({intervalo_confianza[0]:.4f}, {intervalo_confianza[1]:.4f}) pulgadas")

# Crear un histograma de los datos de la muestra
np.random.seed(0)  # Semilla para reproducibilidad
muestras = np.random.normal(media_muestral, desviacion_estandar, tamano_muestra)
plt.hist(muestras, bins=10, edgecolor='k', alpha=0.7)
plt.xlabel('Profundidad (pulgadas)')
plt.ylabel('Frecuencia')
plt.title('Histograma de Profundidades de Módulos Conectores')
plt.grid(True)
plt.show()


