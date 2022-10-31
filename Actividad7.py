#Ejercicio 7
#Realizar una algoritmo que muestre la tabla de multiplicar de un número introducido por teclado.

num = 0

num = int(input("Dime un número: \n"))

print(f"La tabla de multiplicar de {num} es:")

for numero in range (0,11):
    
    print(num*numero)