#Realice un programa que permita ingresar un número mayos o igual a 2 y determine si es un número primo.

print("Ingrese un numero mayor o igual a 2")
numero = int(input())
primo = True
if numero >= 2:
    for i in range(2,numero):
        if numero % i == 0:
            primo=False
            break

    if primo:
        print("es un numero primo" , )
    else:
        print("no es primo")