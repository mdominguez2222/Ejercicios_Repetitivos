#Ejercicio 11
#Escribe un programa que diga si un número introducido por teclado es o no primo. Un número primo es aquel que sólo es divisible entre él mismo y la
#unidad. Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es divisible por algún otro número

num = 0

num = int(input("Dime un número:\n"))
raiz = int(num**(1/2))
divisible = 0

for numero in range (1,raiz+1):
    if(num%numero==0):
        divisible += 1

if (divisible==1):
    print(f"{num} es primo")
else:
    print(f"{num} no es primo")