#Ejercicio 3
#Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir lasuma y la media de todos los números introducidos.

num = 1
suma = 0
contador = -1

print ("Escribe número 0 para salir")


while (num!=0): 
    num = int(input("Dime un número: \n"))  
    suma = suma + num
    contador= contador+1
             
print (f"La suma es {suma}")
print (f"La media es {suma/contador}")