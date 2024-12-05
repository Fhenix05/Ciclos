"""
Programa que pida 10 números e imprima el promedio de estos.

Se utilizan los conceptos del programa anterior de contador y acumulador.
"""

suma = 0
for i in range(10):
    numero = int(input("Ingresa un número: "))
    suma += numero

print("El promedio de los números es", suma / 10) 