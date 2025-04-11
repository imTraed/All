print(">>>>>>>>>>>>> Funciones <<<<<<<<<<<<<<")
print(">>>> Realizado por: Joshua Jacome <<<<")
print(">>>>>>>>>> Fecha: 9/12/2024 <<<<<<<<<<")
print("--------------------------------------")

def datos():
    while True:
        try:
            dato1 = int(input("Ingresa tu primer dato: "))
            break
        except ValueError:
            print("Numero incorrecto")
    while True:
        try:
            dato2 = int(input("Ingresa tu segundo dato: "))
            break
        except ValueError:
            print("Numero incorrecto")
    return dato1, dato2

def menu():
    print("OPERACION CON 2 NUMEROS CON LAS SIGUIENTES OPCIONES")
    print("---------------------------------------------------")
    print("1.Suma    <<<<<<<<<<<<<")
    print("2.Resta   <<<<<<<<<<<<<")
    print("3.Division   <<<<<<<<<<")
    print("4.Multiplicacion  <<<<<")
    print("5.Residuo  <<<<<<<<<<<<")
    print("6.Potencia  <<<<<<<<<<<")
    print("7.Par o Impar  <<<<<<<<")
    print("8.Primo   <<<<<<<<<<<<<")
    print("9.Salir   <<<<<<<<<<<<<")
    print("---------------------------------------------------")

while True:
    menu()

    try:
        opcion = int(input("Selecciona la opción que deseas: "))
    except ValueError:
        print("Opción no válida")
        continue

    if opcion == 1:
        dato1, dato2 = datos()
        print(f"La suma de tus datos es {dato1 + dato2}")
    elif opcion == 2:
        dato1, dato2 = datos()
        print(f"La resta de tus datos es {dato1 - dato2}")
    elif opcion == 3:
        dato1, dato2 = datos()
        try:
            print(f"La división de tus datos es {dato1 / dato2}")
        except ZeroDivisionError:
            print("No se puede dividir por cero")
    elif opcion == 4:
        dato1, dato2 = datos()
        print(f"La multiplicación de tus datos es {dato1 * dato2}")
    elif opcion == 5:
        dato1, dato2 = datos()
        try:
            print(f"El residuo de la división de tus datos es {dato1 % dato2}")
        except ZeroDivisionError:
            print("No se puede obtener el residuo con divisor cero")
    elif opcion == 6:
        dato1, dato2 = datos()
        print(f"La potencia de tus datos es {dato1 ** dato2}")
    elif opcion == 7:
        dato1, dato2 = datos()
        print(f"{dato1} es {'par' if dato1 % 2 == 0 else 'impar'}, y {dato2} es {'par' if dato2 % 2 == 0 else 'impar'}")
    elif opcion == 8:
        dato1, dato2 = datos()
        for numero in [dato1, dato2]:
            if numero < 2:
                print(f"{numero} no es primo")
            else:
                for i in range(2, numero):
                    if numero % i == 0:
                        print(f"{numero} no es primo")
                        break
                else:
                    print(f"{numero} es primo")
    elif opcion == 9:
        print("Fin del programa")
        break
    else:
        print("Opción no válida, por favor selecciona una opción del menú.")

