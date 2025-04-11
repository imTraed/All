'''
Realice un programa que permita usar el siguiente menú:
1. Área del Cuadrado
2. Área del Rectángulo
3. Área del Círculo
4. Salir
'''

print("Menu")
print("1. Área del Cuadrado")
print("2. Área del Rectángulo")
print("3. Área del Círculo")
print("4. Salir")
menu = int(input())

if menu == 1:
    firstd = int(input("ingrese su primera dimension: "))
    second = int(input("ingrese su segunda dimension: "))
    areac = firstd * second
    print(f"El area del cuadrado es {areac}")

if menu == 2:
    base = int(input("ingrese su base: "))
    altura = int(input("ingrese su altura: "))
    arear = base * altura / 2
    print(f"El area del Rectangulo es {arear}")

if menu == 3:
    radio = int(input("ingrese su radio: "))
    areac = 3.14 * radio**2
    print(f"El radio del Circulo es {areac}")

if menu == 4:
    print("Adios")
else:
    print("Opcion invalida") 
