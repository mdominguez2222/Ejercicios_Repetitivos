#Ejercicio 5
#Algoritmo que pida caracteres e imprima ‘VOCAL’ si son vocales y ‘NO VOCAL’ en caso contrario, el programa termina cuando se introduce un espacio.

letra=""

def VocalNoVocal(letra):
    if letra in ("a","e","i","o","u"):
        return "VOCAL"
    else:
        return "NO VOCAL"

while (letra!=" "):
    letra = input("Dime una letra: \n")
    print (VocalNoVocal(letra))

print ("Has salido")