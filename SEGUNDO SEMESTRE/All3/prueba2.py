nombres = []
temperaturas1=[]
temperaturas2=[]
temperaturas3=[]
print("*************************************************")
print("Autores: Erick Moreno, Joshua Jacome")
print("*************************************************")

def lista():
    estudiante = int(input("Ingrese el numero de niños: "))
    for i in range (estudiante):
        nombre = input(f"Ingrese el nombre del niño {i}: ")
        temp1 = float(input("Ingrese la temperatura del dia 1: " ))
        while temp1 < 0:
            print("Error, escribe una temperatura mayor ")
            temp1 = float(input("Ingrese nuevamente la temperatura del dia 1: "))
        temp2 = float(input("Ingrese la temperatura del dia 2: " ))
        while temp2 < 0:
            print("Error, escribe una temperatura mayor ")
            temp2 = float(input("Ingrese nuevamente la temperatura del dia 2: "))
        temp3 = float(input("Ingrese la temperatura del dia 3: " ))
        while temp3 < 0:
            print("Error, escribe una temperatura mayor ")
            temp3 = float(input("Ingrese nuevamente la temperatura del dia 3: "))
        nombres.append(nombre)
        temperaturas1.append(temp1)
        temperaturas2.append(temp2)
        temperaturas3.append(temp3)

def promedioniño():
    for i in range(len(nombres)):
        promedio = (temperaturas1[i] + temperaturas2[i] + temperaturas3[i]) / 3
        print(f"Promedio de {nombres[i]}: {promedio:.2f}")

def promediodia():



    for i in range(len(temperaturas1)):
        promediodia1 = (temperaturas1[i]) / len(temperaturas1)
    print(f"Promedio del día 1: {promediodia1:.2f}")


lista()
while True:
    print(">>>>>> MENU DE REGISTRO DE NIÑOS <<<<<<<")
    print("1.Promedio de cada niño <<<<<<<")
    print("2.Promedio de todos los niños por cada dia <<<<<<<")
    print("3.Tabla de niños segun sus temperaturas del tercer dia <<<<<<<")
    print("4.Salir <<<<<<<")
    opcion=int(input("Ingrese la opcion que necesite: "))
    if opcion == 1:
        promedioniño()
        input("Presione enter para salir")
    elif opcion == 2:
        promediodia()
        input("Presione enter para salir")
    elif opcion == 3:
        "x"
        input("Presione enter para salir")
    elif opcion == 4:
        print("Salir")
        break
    else:
        print("Opción no válida. Intente nuevamente.")



