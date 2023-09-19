"""
@author: diego Quiros
Practica 3 Ejercicio 1
"""

import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# Datos
media_muestral = 780
desviacion_estandar = 40
tamano_muestra = 30
nivel_confianza = 0.96

# Calcular el intervalo de confianza
z = stats.norm.ppf((1 + nivel_confianza) / 2)
error_estandar = desviacion_estandar / np.sqrt(tamano_muestra)
intervalo_confianza = (media_muestral - z * error_estandar, media_muestral + z * error_estandar)

# Imprimir el intervalo de confianza
print(f"Intervalo de confianza del {nivel_confianza * 100}%: ({intervalo_confianza[0]:.2f}, {intervalo_confianza[1]:.2f}) horas")

# Crear un histograma de los datos
np.random.seed(0)  # Semilla para reproducibilidad
muestras = np.random.normal(media_muestral, desviacion_estandar, tamano_muestra)
plt.hist(muestras, bins=10, edgecolor='k', alpha=0.7)
plt.xlabel('Duración de Vida (horas)')
plt.ylabel('Frecuencia')
plt.title('Histograma de Duración de Vida de Focos')
plt.grid(True)
plt.show()
