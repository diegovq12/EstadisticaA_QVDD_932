# -*- coding: utf-8 -*-
"""
@author: diego
Practica 3 ejercicio 3
"""
import scipy.stats as stats
import numpy as np
import matplotlib.pyplot as plt

# Datos
media_muestral = 3.0  # Precio medio muestral
desviacion_estandar_muestral = 1.6  # Desviación estándar muestral
tamano_muestra = 48
nivel_confianza = 0.95

# Calcular el intervalo de confianza para la media
grados_libertad = tamano_muestra - 1
t_valor = stats.t.ppf((1 + nivel_confianza) / 2, df=grados_libertad)
error_estandar = desviacion_estandar_muestral / np.sqrt(tamano_muestra)
intervalo_confianza = (media_muestral - t_valor * error_estandar, media_muestral + t_valor * error_estandar)

# Imprimir el intervalo de confianza
print(f"Intervalo de confianza del {nivel_confianza * 100}% para la media: ({intervalo_confianza[0]:.4f}, {intervalo_confianza[1]:.4f})")

# Calcular el error estándar de la estimación
error_estandar_estimacion = t_valor * desviacion_estandar_muestral / np.sqrt(tamano_muestra)

# Imprimir el error estándar de la estimación
print(f"Error estándar de la estimación: {error_estandar_estimacion:.4f}")

# Crear un histograma de los precios
np.random.seed(0)  # Semilla para reproducibilidad
precios = np.random.normal(media_muestral, desviacion_estandar_muestral, tamano_muestra)
plt.hist(precios, bins=10, edgecolor='k', alpha=0.7)
plt.xlabel('Precio (dólares)')
plt.ylabel('Frecuencia')
plt.title('Histograma de Precios de Arroz en Tiendas de Ensenada')
plt.grid(True)
plt.show()


