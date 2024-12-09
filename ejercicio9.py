"""
Escribe un programa que pida el limite inferior y superior de un intervalo. 
Si el límite inferior es mayor que el superior lo tiene que volver a pedir.
A continuación se van introduciendo números hasta que introduzcamos el 0. 
Cuando termine el programa dará las siguientes informaciones:
	* La suma de los números que están dentro del intervalo (intervalo abierto).
	* Cuantos números están fuera del intervalo.
	* He informa si hemos introducido algún número igual a los límites del intervalo.
"""

while True:
    limin = int(input("Ingrese el límite inferior del intervalo: "))
    limsu = int(input("Ingrese el límite superior del intervalo: "))
    if limin < limsu:
        break
    print("El límite inferior debe ser menor que el límite superior. Inténtelo de nuevo.")

suma_dentro_intervalo = 0
numeros_fuera_intervalo = 0
igual_a_limites = False

while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    if num == 0:
        break

    if limin < num < limsu:
        suma_dentro_intervalo += num
    else:
        numeros_fuera_intervalo += 1

    if num == limin or num == limsu:
        igual_a_limites = True

print("\nResultados:")
print(f"Suma de los números dentro del intervalo abierto ({limin}, {limsu}): {suma_dentro_intervalo}")
print(f"Cantidad de números fuera del intervalo: {numeros_fuera_intervalo}")
print(f"Se ha introducido algún número igual a los límites: {'Sí'if igual_a_limites else 'No'}")