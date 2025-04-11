import random
ejercicios = ['Piernas', 'Bicep', 'Tricep', 'Pecho', 'Espalda','Hombros']
while True:
    print("")
    print('1. Número aleatorio entre 1 y 100:')
    print("2. Ejercicio aleatorio elegida")
    print("3. Lista de ejercicios mezclada aleatoriamente")
    print("4. Número decimal aleatorio entre 0 y 1")
    print("5. Salir")
    opcion = int(input("Elije la opcion que necesitas: "))
    while opcion < 0 or opcion > 7:
        print("Error, opcion no valida")
        break

    if opcion == 1:
        numaleatorio = random.randint(1, 100)
        print(numaleatorio)

    elif opcion == 2:
        frutaaleatoria = random.choice(ejercicios)
        print(frutaaleatoria)

    elif opcion == 3:
        random.shuffle(ejercicios)
        print(ejercicios)

    elif opcion == 4:
        numdecimal = random.random()
        print(numdecimal)

    elif opcion == 5:
        print("Gracias por usar el programa")
        break