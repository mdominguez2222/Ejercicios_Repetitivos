'''
Ejercicio 18
Hacer un programa que muestre un cronometro, indicando las horas, minutos y
segundos.
'''

import os

cantidad_horas=0
cantidad_minutos=0
cantidad_segundos=0

for cantidad_horas in range(24):
    os.system('cls')
    for cantidad_minutos in range(60):
        for cantidad_segundos in range(60):
            print(f"{cantidad_horas}h : {cantidad_minutos}' : {cantidad_segundos}''")