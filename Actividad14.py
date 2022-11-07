'''
Ejercicio 14
Una persona se encuentra en el kilómetro 70 de una carretera, otra se encuentra
en el km 150, los coches tienen sentido opuesto y tienen la misma velocidad.
Realizar un programa para determinar en qué kilómetro de esa carretera se
encontrarán.

'''

a = 70
b = 150
d = b-a

while (d>0):
    a += 1
    b -= 1 
    d = b-a

print (f"Se encotrarán en el kilómetro {a}")