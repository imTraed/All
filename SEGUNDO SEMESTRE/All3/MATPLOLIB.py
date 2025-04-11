import matplotlib.pyplot as plt
estado = ["Desaprobados", "Aprobados", "En espera"]
num = [2, 10, 7]

while True:
    print("GRAFICAS DE NOTAS CON ESTUDIANTES")
    print('1. BARRAS DE LOS ESTUDIANTES SEGUN SU ESTADO')
    print("2. PASTEL CON EL PORCENTAJE DE LOS ESTUDIANTES SEGUN SU ESTADO")
    print("3. GRAFICO DE LINEAS CON LOS DATOS DE ESTUDIANTES")
    print("4. HISTOGRAMA CON LAS NOTAS DE ESTUDIANTES")
    print("5. SALIR")
    opcion = int(input("Elije la opcion que necesitas: "))
    while opcion < 0 or opcion > 5:
        print("Error, opcion no valida")
        break
    if opcion == 1:

        plt.bar(estado, num)
        plt.title("----- Numero de personas según su estado -----")
        plt.xlabel(">>>>>  ESTADO  <<<<<")
        plt.ylabel(">>>>  NUM PERSONAS  <<<<")
        plt.show()

    elif opcion == 2:
        plt.pie(num, labels=estado, autopct='%1.1f%%', startangle=90)
        plt.title("----- Porcentaje de personas según su estado -----")
        plt.show()

    elif opcion == 3:
        plt.plot(estado, num, marker='o')
        plt.title("----- Numero de personas según su estado -----")
        plt.xlabel(">>>>>  ESTADO  <<<<<")
        plt.ylabel(">>>>  NUM PERSONAS  <<<<")
        plt.grid(True)
        plt.show()

    elif opcion == 4:
        notas = [72, 85, 92, 78, 65, 88, 95, 60, 70, 82, 90, 76, 
        84, 73, 88, 79, 93, 68, 87, 91]
        plt.hist(notas, bins=10, edgecolor='black')
        plt.title('Notas de exámenes')
        plt.xlabel('Calificaciones')
        plt.ylabel('Frecuencia')
        plt.show()
    elif opcion == 5:
        print("Gracias por usar el programa")
        break

