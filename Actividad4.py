#Ejercicio 4
#Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de números a introducir). El programa debe informar de cuantos números
#introducidos son mayores que 0, menores que 0 e iguales a 0.

num = 0
numero = 0
contador = 0
mayor = 0
igual = 0
menor = 0

num = int (input("Cantidad de números que vas a introducir: \n"))

while (num!=contador):
    numero = int (input("Dime un número: \n"))
    contador += 1
    if (numero < 0):
        menor += 1

    elif (numero > 0):
        mayor += 1

    elif (numero==0):
        igual += 1

print (f"Has introducido {menor} número/s menor/es que 0, {mayor} mayor/es que 0 y {igual} igual/es a 0")