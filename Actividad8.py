#Ejercicio 8
'''
Escribe un programa que pida el limite inferior y superior de un intervalo. Si el
límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0.
Cuando termine el programa dará las siguientes informaciones:
 -La suma de los números que están dentro del intervalo (intervalo abierto).
 -Cuantos números están fuera del intervalo.
 -He informa si hemos introducido algún número igual a los límites del intervalo'''

#Función que devuelve una lista de números introducidos

def pideNumeros():
    vNum = []
    num = 1
    while (num!=0):
        try:
            contador = len(vNum)
            num = int(input(f"Dime el número {len(vNum)}\n"))
            if (num!=0):
                vNum.append(num)
        except:
            print("Tienes que introducir números")
    return vNum


def realizarCalculos(vDatos,limiteInferior,limiteSuperior):
    suma = 0
    fuera = 0
    igualesAlimites = 0
    vLimites = list(range(limiteInferior+1,limiteSuperior))
    for i in vDatos:
        if (i in vLimites):
            suma += i
        else:
            fuera += 1
        if (i==limiteInferior or i==limiteSuperior):
            igualesAlimites +=1

    print("La suma total dentro de los límites es:", suma)
    print(f"Has introducido {fuera} números fuera de los límites")
    print(f"Has introducido {igualesAlimites} números iguales a los límites")



#Pedir Límites Inferior y Superior

limiteInferior = 1
limiteSuperior = 0

while limiteInferior > limiteSuperior:
    try:
        limiteInferior = int(input("Dime el límite inferior:\n"))
        limiteSuperior = int(input("Dime el límite superior:\n"))
        if limiteInferior > limiteSuperior:
            print("Es obligatorio que el límite inferior sea menor que el superior:\n")
            print("*********\n")
    except:
        print("Tienes que introducir números")


#Pido los números

vNum = pideNumeros()
print (vNum)


#Realizar cálculos

realizarCalculos(vNum,limiteInferior,limiteSuperior)