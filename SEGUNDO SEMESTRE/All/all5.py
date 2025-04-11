"""
Realice un programa que permita ingresar un 
número entero positivo y calcule la serie de Fibonacci hasta ese número. 
La serie debe mostrarse en pantalla de forma ordenada.
"""

n = int(input("Ingrese un número entero positivo para la serie de Fibonacci: "))

if n <= 0:
    print("Por favor, ingrese un número mayor a 0.")
else:
    fib_series = [0, 1]

    while len(fib_series) < n:
        nuevo_numero = fib_series[len(fib_series) - 1] + fib_series[len(fib_series) - 2]
        fib_series += [nuevo_numero]

    print(f"La serie de Fibonacci hasta {n} es: {fib_series[:n]}")
