'''
Ejercicio 20
Mostrar en pantalla los N primero número primos. Se pide por teclado la cantidad 
de números primos que queremos mostrar.
'''
import math
 
numVeces = int(input('¿Cuántos primos quieres?: '))
p = 1   
c = 3   
r = '2' 
while (p < numVeces):
    fact1 = math.factorial(c-1)
    if fact1 % c == c-1:
        r += ', ' + str(c)
        p += 1  
    c += 1      
print(r)