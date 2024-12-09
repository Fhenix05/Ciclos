"""
Realizar un programa para determinar cuánto ahorrará una persona en un año, 
si al final de cada mes deposita cantidades variables de dinero; 
además, se quiere saber cuánto lleva ahorrado cada mes.
"""

def main():
    # Inicializar variables
    ahorros_totales = 0
    ahorros_mensuales = []

    print("Ahorro mensual:")
    for mes in range(1, 13):  # De enero (1) a diciembre (12)
        while True:
            try:
                deposito = float(input(f"Ingrese el monto ahorrado en el mes {mes}: "))
                if deposito < 0:
                    print("El monto no puede ser negativo. Inténtalo de nuevo.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número válido.")

        # Actualizar ahorros
        ahorros_totales += deposito
        ahorros_mensuales.append(ahorros_totales)

        # Mostrar acumulado del mes
        print(f"Total acumulado al final del mes {mes}: {ahorros_totales:.2f} unidades monetarias.\n")

    # Resultados finales
    print("Resumen anual:")
    for i, acumulado in enumerate(ahorros_mensuales, start=1):
        print(f"Mes {i}: {acumulado:.2f} unidades monetarias acumuladas.")

    print(f"\nEl total ahorrado al final del año es: {ahorros_totales:.2f} unidades monetarias.")

if __name__ == "__main__":
    main()