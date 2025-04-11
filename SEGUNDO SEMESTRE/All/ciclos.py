print("*************************************************")
print("Autores:Joshua Jacome")
print("Fecha: 09/10/2024")
print("Impresion de pares")
print("*************************************************")

limite = int(input("Ingrese el limite de numeros:"))
while limite <=0:
    print("se reciben numeros positivos")
    limite = int(input("Ingrese el limite de numeros:"))
numero = 0
while numero <= limite:
    if numero % 2 == 0:
        print  (numero , end= " , " )
    numero += 1

