"""
Una persona adquirió un producto para pagar en 20 meses. El primer mes pagó 10 
euros, el segundo 20 euros, el tercero 40 euros y así sucesivamente. 
Realizar un programa para determinar cuánto debe pagar mensualmente y el total 
de lo que pagó después de los 20 meses.
"""

a1 = 10  
meses = 20

pagos_mensuales = []
suma_total = 0
for n in range(1, meses + 1):
    pago_mensual = a1 * (2 ** (n - 1))
    pagos_mensuales.append(pago_mensual)
    suma_total += pago_mensual

print("Pagos mensuales:")
for i, pago in enumerate(pagos_mensuales, start=1):
    print(f"Mes {i}: {pago} euros")

print(f"\nTotal pagado después de {meses} meses: {suma_total} euros")