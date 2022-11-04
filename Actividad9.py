#Ejercicio 9
#Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede
#utilizar el operador de potencia.

exponente = 1


def calculaPotencia(base,exponente):
    return base^exponente


num = int(input("¿Cuántas veces quieres calcular una potencia?\n"))


while (exponente>0):
    try:
        for i in range(0,num):
            base = int(input("Dime la base:\n"))
            exponente = int(input("Dime el exponente\n"))   

            print (f"La potencia es {calculaPotencia(base,exponente)}")
            print("\n")
            print ("***********")

        if (exponente<0):
            print("El exponente tiene que ser positivo\n")

    except:
        print("Tienes que introducir números")
        

    
