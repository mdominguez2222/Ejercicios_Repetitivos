'''
Ejercicio 20
Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad 
de números primos que queremos mostrar.
'''

numero = 1
divisible = 0
num = 1
n = 0
cont = 1
n = int(input("¿Cuántos primos quieres?: \n"))

def esPrimo (num):
    for prim in range (2,n):
        if(num%prim==0):
            return False
    return True   


while (n!=0):
    if (esPrimo(cont)==True):
        print(cont)
        n-=1

    cont += 1