print("*************************************************")
print("Autores:Joshua Jacome")
print("Fecha: 09/10/2024")
print("*************************************************")

numero = int(input(""))
while numero < 2:
    print("ingrese numeros positivos")
    numero = int(input())
    
for i in range(1,numero+1):
    print(numero, "/" , i , "=" , numero / i)

if numero / 1 == numero:
    print("es numero primo")
else:
    print("no es numero primo")

