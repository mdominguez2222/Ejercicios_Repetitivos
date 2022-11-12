'''
Ejercicio 16
Una empresa les paga a sus empleados con base en las horas trabajadas en la
semana. Realice un algoritmo para determinar el sueldo semanal de N
trabajadores y, además, calcule cuánto pagó la empresa por los N empleados.
'''

sueldo = 0
sueldototal = 0

trabajadores = int(input("¿Cuántos trabajadores son?: \n"))
horas = int(input("¿Cuántas horas trabajan al día?:\n"))
sueldoHora = int(input("Sueldo por hora:\n"))

for i in range (0,5):
    sueldo += (sueldoHora*horas)

sueldototal = trabajadores*sueldo
print(f"El sueldo semanal de un trabajador es {sueldo}€")
print(f"La empresa ha pagado {sueldototal}€ por los {trabajadores} trabajadores")