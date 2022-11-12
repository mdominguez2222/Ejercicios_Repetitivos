'''
Ejercicio 19
Realizar un ejemplo de menú, donde podemos escoger las distintas opciones 
hasta que seleccionamos la opción de “Salir”.
'''


opcion = 0

while (opcion != 4):

    print("OPCIÓN 1: suma de dos números")
    print("OPCIÓN 2: producto de dos números")
    print("OPCIÓN 3: división de dos números")
    print("OPCIÓN 4: salir")
    print("**************")
    opcion = int(input("Elige una opción: \n"))

    try:
        if (opcion==1):
            num1 = int(input("Dime un número: \n"))
            num2 = int(input("Dime otro número: \n"))
            print (f"La suma de ambos es {num1+num2}")
            print("************")
        elif (opcion==2):
            num1 = int(input("Dime un número: \n"))
            num2 = int(input("Dime otro número: \n"))
            print(f"El producto de ambos es {num1*num2}")
            print("************")            
        elif (opcion==3):
            num1 = int(input("Dime un número: \n"))
            num2 = int(input("Dime otro número: \n"))
            print(f"La división de ambos es {num1/num2}")
            print("************")
    except:
        print("Elige una opción, de la 1 a la 4")

print("Has salido")