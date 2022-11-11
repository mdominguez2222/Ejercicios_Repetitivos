'''
Ejercicio 13
Una empresa tiene el registro de las horas que trabaja diariamente un empleado
durante la semana (seis días) y requiere determinar el total de éstas, así como el
sueldo que recibirá por las horas trabajadas.
'''

horasDiarias = 0
total = 0
sueldo = 0

sueldo = int(input("Sueldo por hora: \n"))

for i in range (0,6):
    horasDiarias = int(input("Horas trabajadas cada día de la semana: \n"))
    total = horasDiarias+total
sueldo = sueldo*total
print (f"El sueldo total es {sueldo}€ y el total de horas trabajadas es {total} horas")