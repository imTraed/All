nombres = []
temperaturas1 = []
temperaturas2 = []
temperaturas3 = []

def lista():
    estudiante = int(input("Ingrese el numero de niños: "))
    for i in range(estudiante):
        nombre = input(f"Ingrese el nombre del niño {i+1}: ")
        temp1 = float(input("Ingrese la temperatura del dia 1: "))
        while temp1 < 0:
            print("Error, escribe una temperatura mayor")
            temp1 = float(input("Ingrese nuevamente la temperatura del dia 1: "))
        temp2 = float(input("Ingrese la temperatura del dia 2: "))
        while temp2 < 0:
            print("Error, escribe una temperatura mayor")
            temp2 = float(input("Ingrese nuevamente la temperatura del dia 2: "))
        temp3 = float(input("Ingrese la temperatura del dia 3: "))
        while temp3 < 0:
            print("Error, escribe una temperatura mayor")
            temp3 = float(input("Ingrese nuevamente la temperatura del dia 3: "))
        nombres.append(nombre)
        temperaturas1.append(temp1)
        temperaturas2.append(temp2)
        temperaturas3.append(temp3)

def promedio_por_nino():
    for i in range(len(nombres)):
        promedio = (temperaturas1[i] + temperaturas2[i] + temperaturas3[i]) / 3
        print(f"Promedio de {nombres[i]}: {promedio:.2f}")

def promedio_por_dia():
    promedio_dia1 = sum(temperaturas1) / len(temperaturas1)
    promedio_dia2 = sum(temperaturas2) / len(temperaturas2)
    promedio_dia3 = sum(temperaturas3) / len(temperaturas3)
    print(f"Promedio del día 1: {promedio_dia1:.2f}")
    print(f"Promedio del día 2: {promedio_dia2:.2f}")
    print(f"Promedio del día 3: {promedio_dia3:.2f}")

def tabla_tercer_dia():
    print("\nTabla de niños según sus temperaturas del tercer día:")
    sorted_indices = sorted(range(len(temperaturas3)), key=lambda i: temperaturas3[i], reverse=True)
    for i in sorted_indices:
        print(f"{nombres[i]}: {temperaturas3[i]}")

lista()

while True:
    print("\n1. Promedio de cada niño")
    print("2. Promedio de todos los niños por cada día")
    print("3. Tabla de niños según sus temperaturas del tercer día")
    print("4. Salir")
    
    opcion = int(input("Ingrese la opción que necesite: "))
    
    if opcion == 1:
        promedio_por_nino()
    elif opcion == 2:
        promedio_por_dia()
    elif opcion == 3:
        tabla_tercer_dia()
    elif opcion == 4:
        print("Saliendo...")
        break
    else:
        print("Opción no válida. Intente nuevamente.")
