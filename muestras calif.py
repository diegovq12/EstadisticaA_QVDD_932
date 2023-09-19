"""
EJERCICIO. Calcula el intervalo de condianza
ejercicio: simule las calificaciones de 300 estudiantes,
en un intervalo del 0 al 100 (solo numeros enteros), despues 
calcule la media y la desviacion estandar de la muestra.
Despues calcule un intervalo de confianza del 99%  de la 
calificacion promedio de estas calificaciones , repita el experimento, 
pero ahora para 1000 estudiantes.
cual es su opinion respecto al efecto del tamano de la muestra?

"""

#generar las calificaciones
import random
import statistics as st

calificaciones=range(0,101,1)
len(calificaciones)
poblacion=list(calificaciones)
print(poblacion) #imprimir poblacion

#muestra de 300 con reemplazo
n300=random.choices(poblacion,k=300)# este es un vector
n=len(n300) ##para llevar el valor de 300
print(n)

#Calcular media

media_n300=st.mean(n300)
print("La media de n=300 es = ",media_n300)#imprimimos la media

#calcular desviacion estandar de la muestra
dv_n300=st.stdev(n300)
print("La desviacion estandar de n=300 es =",dv_n300)
#La desviacion estandar de n=300 es -
##alfa=0.01 entonces alfa/2=0.005
# por lo cual z=2.575

z=2.575

# el intervalo de confianza es:
#inferior
x_inf=((media_n300)-(z)*((dv_n300)/(n**0.5)))
#superior
x_sup=((media_n300)+(z)*((dv_n300)/(n**0.5)))

""" El valor de la media esta dentro del intervalo"""

#El rango de la media poblacional es:

rango_mu=x_sup-x_inf

rango_mu
print(rango_mu)

"""AHORA PARA MUESTRA DE N=1000"""

print("Prueba de 1000\n")

n1000=random.choices(poblacion,k=1000)
n2=len(n1000)
print(n2)

media_n1000=st.mean(n1000)
print("La media de n=1000 es= ",media_n1000)

dv_n1000=st.stdev(n1000)
print("La desviacion estandar de n=1000 es= ",dv_n1000)

z=2.575#nota: de donde sale z?

# el intervalo de confianza es:
#inferior
x_inf=((media_n1000)-(z)*((dv_n1000)/(n2**0.5)))
#superior
x_sup=((media_n1000)+(z)*((dv_n1000)/(n2**0.5)))


rango_mu=x_sup-x_inf

rango_mu
print(rango_mu)

