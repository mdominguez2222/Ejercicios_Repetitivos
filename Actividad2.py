#Ejercicio 2
#Crea una aplicación que permita adivinar un número. La aplicación genera unnúmero aleatorio del 1 al 100. A continuación va pidiendo números y va
#respondiendo si el número a adivinar es mayor o menor que el introducido,a demás de los intentos que te quedan (tienes 10 intentos para acertarlo). El
#programa termina cuando se acierta el número (además te dice en cuantos intentos lo has acertado), si se llega al limite de intentos te muestra el número
#que había generado.

import random

numero = random.randint(1,100)
num = 0
fallos = 0

while (numero!=num and fallos<10):
    fallos += 1
    num = int(input("Dime un número: \n"))
    if (numero<num):
        print("El número es menor")
    else:
        print("El número es mayor")


if (fallos==10):
    print (f"Has llegado al límite de intentos. El número era {numero}")
else:
    print (f"Lo has adivinado. Has hecho {fallos} intentos")