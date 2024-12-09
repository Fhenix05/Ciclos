"""
Mostrar en pantalla los N primero números primos. Se pide por teclado la cantidad 
de números primos que queremos mostrar.
"""

def es_primo(numero):
    if numero <= 1:
        return False 
    for i  in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False
    return True

n = int(input("Introduce la cantidad de números primos que quieres mostrar: ")) 

primos = []
numero = 2

while len(primos) < n:
    if es_primo(numero):
        primos.append(numero)
    numero += 1

print(f"Los primeros {n} números primos son:")
print(primos)