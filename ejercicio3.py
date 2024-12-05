"""
Algoritmo que pida números hasta que se introduzca un cero. Debe imprimir la suma
y la media de todos los números introducidos.

Para este problema se requiere de un acumulador y un contador

Contador: Variable que va, como su nombre lo indica, contando elementos (iteraciones),
por cada iteración el contador va incrementando en 1

Ejemplo:
contador = 0
for i in range(5):
    contador = contador + 1
print(contador)

Acumulador: Variable que va, como su nombre lo indica, acumulando valores en cada iteración,
por cada iteración al valor inicial se le suman nuevos valores al acumulador

Ejemplo:
acumulador = 0;
for i in range(5):
    acumulador = acumulador + i
print(acumulador)
"""

contador = 0
suma = 0
while True:
    numero = int(input("Ingresa un número\n 0 para salir: "))
    if numero == 0:
        break
    else:
        suma = suma + numero 
        contador = contador + 1 

print("La suma de los número ingresadoses:", suma)
print("El promedio de los números es:", suma / contador)