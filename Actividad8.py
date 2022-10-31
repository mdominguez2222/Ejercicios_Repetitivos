#Ejercicio 8
'''
Escribe un programa que pida el limite inferior y superior de un intervalo. Si el
límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0.
Cuando termine el programa dará las siguientes informaciones:
 -La suma de los números que están dentro del intervalo (intervalo abierto).
 -Cuantos números están fuera del intervalo.
 -He informa si hemos introducido algún número igual a los límites del intervalo'''

inferior = 0
superior = 0
vNum = []
num = 1
suma = 0
numerosfuera = 0

inferior = int(input("Dime el límite inferior: \n"))
superior = int(input("Dime el límite superior: \n"))

if (inferior>superior):
    inferior = input("El límete inferior tiene que ser menor. Vuelve a introducirlo:\n")
    superior = input("Vuelve a introducir el límite superior:\n")

vLim = []

vLim.insert(0,inferior)
vLim.append(superior)
    
while (num!=0):
    num = int(input("Dime un número:\n"))
    suma += num
    vNum.append(num)

vFuera = []

if (num<inferior or num>superior):
    vFuera.append(num)

print("La suma de los números es", suma)
print(f"Los números que están fuera del intervalo son {len(vFuera)}")