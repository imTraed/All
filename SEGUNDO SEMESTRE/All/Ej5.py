print("Nombre: Joshua Jacome")
print("Fecha: 7/10/2024")
print("*********************")
print('Digita tu edad para saber que entrada te corresponde')
edad = int(input())
price = 10
priceadultos = price -2
if edad <= 4:
    print('Entrada para ninos el costo es de $0')
elif  edad <= 17:
    print('Entrada para jovenes el costo es de $5')
elif  edad <= 64:
    print(f'Entrada para adultos el costo es de {price}')
else:
    print(f'Entrada para mayores el costo es {priceadultos}')



