print("******** Menu de opciones *******")
print("**********  Calculadora **********")
print("1. Suma               ******")
print("2. Resta              ******")
print("3. Multiplicacion     ******")
print("4. Division           ******")
opcion = int(input("**** Elije la opcion que necesitas  ****"))
if opcion < 1 or opcion > 4:
    print("ERROR")
else:
    num1 = float(input("Ingrese su primer numero: "))
    num2 = float(input("Ingrese su segundo numero: "))
    if opcion == 4 and num2 == 0:
        print("ERROR")
    else:
        if opcion == 1:
            suma = num1 + num2
            print(f"Tu suma es {suma} y el tipo es: {type(suma)}")
        elif opcion == 2:
            resta = num1 - num2
            print(f"Tu resta es {resta} y el tipo es: {type(resta)}")
        elif opcion == 3:
            multiplicacion = num1 * num2
            print(f"Tu multiplicación es {multiplicacion} y el tipo es: {type(multiplicacion)}")
        elif opcion == 4:
            division = num1 / num2
            print(f"Tu división es {division} y el tipo es: {type(division)}")