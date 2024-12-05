"""
Realizar un algoritmo que pida números (se pedirá por teclado la cantidad de 
números a introducir). El programa debe informar de cuantos números introducidos 
son mayores que 0, menores que 0 e iguales a 0.
"""
cantidad = int(input("¿Cuántos números quieres leer?\n"))
mayores_a_cero = 0
menores_a_cero = 0
iguales_a_cero = 0
for i in range(cantidad):
    numero = int(input("Ingresa un número:\n"))
    if numero > 0:
        mayores_a_cero += 1
    elif numero < 0:
        menores_a_cero += 1
    else:
        iguales_a_cero += 1
    
print(f'Ingresaste {mayores_a_cero} números mayores a cero')
print(f'Ingresaste {menores_a_cero} números menores a cero')
print(f'INgresaste {iguales_a_cero} números iguales a cero')