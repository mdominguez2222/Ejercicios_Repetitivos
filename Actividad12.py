'''
Ejercicio 12
Realizar un algoritmo para determinar cuánto ahorrará una persona en un año, si
al final de cada mes deposita cantidades variables de dinero; además, se quiere
saber cuánto lleva ahorrado cada mes.
'''

ahorroMes = 0
ahorroAño = 0

vMes = []

for i in range (0,12):
    ahorroMes = int(input("Ahorro del mes: \n"))
    ahorroAño = ahorroMes+ahorroAño
    vMes = ahorroAño
    print(f"Tienes ahorrado: {vMes}€")

print (f"Este año has ahorrado {ahorroAño}€")