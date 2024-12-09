"""
Escribe un programa que dados dos números, uno real (base) y un entero positivo 
(exponente), saque por pantalla el resultado de la potencia. No se puede 
utilizar el operador de potencia.
"""

bas = float(input("Ingrese la base (Número real): "))
exp = int(input("Ingrese el expoenente (Número entero positivo): "))

while exp < 0:
    print("El exponente debe ser un entero positivo.")
    exp = int(input("Ingrese el exponente (un entero positivo): "))

res = 1
for _ in range(exp):
    res *= bas

print(f"El resultado de {bas} elevado a la {exp} es: {res}")