def calculadora():
    print("Seleccione la operación:")
    print("1. Suma")
    print("2. Resta")
    print("3. Multiplicación")
    print("4. División")
    print("5. Potencia")
    print("6. División Entera")
    print("7. Módulo")

    opcion = int(input("Ingrese el número de la operación (1-7): "))

    if opcion < 1 or opcion > 7:
        print("Opción inválida")
        return

    num1 = float(input("Ingrese el primer número: "))
    num2 = float(input("Ingrese el segundo número: "))

    if opcion == 1:
        print(f"Resultado: {num1 + num2}")
    elif opcion == 2:
        print(f"Resultado: {num1 - num2}")
    elif opcion == 3:
        print(f"Resultado: {num1 * num2}")
    elif opcion == 4:
        if num2 != 0:
            print(f"Resultado: {num1 / num2}")
        else:
            print("Error: División por cero")
    elif opcion == 5:
        print(f"Resultado: {num1 ** num2}")
    elif opcion == 6:
        if num2 != 0:
            print(f"Resultado: {num1 // num2}")
        else:
            print("Error: División por cero")
    elif opcion == 7:
        if num2 != 0:
            print(f"Resultado: {num1 % num2}")
        else:
            print("Error: División por cero")
