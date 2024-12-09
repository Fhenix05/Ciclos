"""
Realizar un programa que pida al usuario un número entero y muestre el mismo número en binario
"""

num = int(input("Introduce un número entero: "))
bina = bin(num)[2:]
print(f"El número {num} en binario es: {bina}")