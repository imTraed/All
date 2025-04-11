print("Nombre: Joshua Jacome")
print("Fecha: 7/10/2024")
print("*********************")
print("Ingrese un numero")
num = int(input())
residuo = num % 2
if num == 0:
    print("es igual a cero")
elif residuo == 0:
    print("es par")
else:
    print("es impar")