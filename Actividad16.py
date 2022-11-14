'''
Ejercicio 16
Una empresa les paga a sus empleados con base en las horas trabajadas en la
semana. Realice un algoritmo para determinar el sueldo semanal de N
trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.
'''

horasSemana = 0
trabajadores = 0
sueldo_por_hora = 0
sueldosemanal = 0
horastotal = 0

trabajadores = int(input("¿Cuántos trabajadores son?: \n"))
sueldo_por_hora = int(input("¿Cuánto se cobra por hora?: \n"))

sueldosemanal = sueldo_por_hora*trabajadores

for num in range (1,trabajadores+1):
    horasSemana = int(input(f"¿Cuántas horas trabaja a la semana el empleado {num}?:\n"))
    horastotal += horasSemana

print(f"El sueldo semanal de los {trabajadores} trabajadores es {sueldosemanal}€")
print(f"El sueldo total que paga la empresa es {horastotal*sueldo_por_hora}")