#Ejercicio 9
#Escribe un programa que dados dos números, uno real (base) y un entero positivo (exponente), saque por pantalla el resultado de la potencia. No se puede
#utilizar el operador de potencia.

base = int(float(input("Dime la base:\n")))
exponente = -1

while exponente<0:
    exponente = (int)(input("Dime el exponente:\n"))

potencia = 1
for i in range(1,exponente+1):
    potencia *= base

print(f"{base}^{exponente}= {potencia}")
    
