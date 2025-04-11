# Ejemplo de todos los tipos de estructuras condicionales en Python

# if simple
numero = 10
if numero > 5:
    print("El número es mayor que 5")

# if-else
edad = 18
if edad >= 18:
    print("Eres mayor de edad")
else:
    print("Eres menor de edad")

# if-elif-else
dia = "lunes"
if dia == "lunes":
    print("Hoy es lunes")
elif dia == "martes":
    print("Hoy es martes")
else:
    print("Hoy no es lunes ni martes")

# if anidado
x = 15
if x > 10:
    if x < 20:
        print("El número está entre 10 y 20")
    else:
        print("El número es mayor o igual a 20")
else:
    print("El número es menor o igual a 10")

# if con operadores lógicos
a = 7
b = 12
if a > 5 and b < 15:
    print("a es mayor que 5 y b es menor que 15")
if a < 10 or b > 20:
    print("a es menor que 10 o b es mayor que 20")

