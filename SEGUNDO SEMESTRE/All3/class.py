notas=[10,7,5,3,10]

while True:
    print(">>>>>>>>>>>>MENU<<<<<<<<<<<<<<<<")
    print("1.Longitud  <<<<<<<<<<<<<<<<")
    print("2.Promedio  <<<<<<<<<<<<<<<<")
    print("3.Varianza  <<<<<<<<<<<<<<<<")
    print("4.Salir     <<<<<<<<<<<<<<<<")
    opcion=int(input("Ingrese la opcion que desea: "))

    if opcion == 1:
        longitud = len(notas)
        print(f"La longitud de la las notas es {longitud}")

    elif opcion == 2:
        suma = 0
        for i in range (len(notas)):
            suma += notas[i]
        div = suma / len(notas)
        print(f"El promedio es {div}")

    elif opcion == 3:
        numerador = 0
        for i in range (len(notas)):
            numerador += ((notas[i] - div)**2)
        varianza = numerador/(len(notas)-1)
        print(f"La varianza es {varianza}")

    elif opcion == 4:
        print("Saliendo del programa")
        break

    else:
        print ("Opcion no valida")




