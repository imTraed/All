print("Nombre: Joshua Jacome")
print("Fecha: 7/10/2024")
print("*********************")
print('Ingrese sus 3 valores cuatrimestralesd de sus ingresos al año')
primero = int(input('-Primer Valor  '))
segundo = int(input('-Segundo Valor  '))
tercero =int(input('-Tercer Valor   '))
suma = (primero + segundo + tercero)
promedio = suma / 3
print(f'La suma en total es {suma}')
if suma < 5000:
    impuestos = 0.1
elif  suma < 10000:
    impuestos = 0.2
else:
    impuestos = 0.4
impay  = suma * impuestos
print(f'El promedio de ingresos es {suma}')
print(f'Los impuestos son {impay}')




