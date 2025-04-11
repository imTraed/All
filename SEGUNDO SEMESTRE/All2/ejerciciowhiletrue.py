while True:
    print("1.Area del circulo")
    print("2.Area del cuadrado")
    print("3.salir")
    opcion = int(input("Seleccione una opcion: "))
    while opcion <= 0 or opcion>3:
        print("error solo hay 3 opciones en el menu")
        opcion = int(input("seleccione la opcion correcta"))
    if opcion == 1:
        print("Area del circulo")
        radio = float(input("ingrese el radio del circulo"))
        areacir = 3.14*(radio**2)
        print(f"el area es {areacir}")
    elif opcion == 2:
        print("Area del cuadrado")
        lado = float(input("ingrese el lado del cuadrado"))
        areacuad = lado * lado
        print(f"el area es {areacuad}")
    elif opcion == 3:
        print("saliendo")
        break


