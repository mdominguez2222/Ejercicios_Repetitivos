#Ejercicio 1
#Crea una aplicación que pida un número y calcule su factorial (El factorial de un número es el producto de todos los enteros entre 1 y el propio número y se
#representa por el número seguido de un signo de exclamación. Por ejemplo 5! =1x2x3x4x5=120)

'''

num = 0
num = int(input("Dime un número para calcular su factorial: \n"))

resultado = 1

for num in range (1,num+1):
    resultado = resultado * num

print(f"El factorial de {num} es {resultado}")
'''

#CON WHILE:

num = 0
num = int(input("Dime un número para calcular su factorial: \n"))
contador = num
resultado = 1

while(contador):

    resultado *= contador
    contador -= 1

print(f"El factorial de {num} es {resultado}")