from funciones import regpaciente, addestado, mostrarpaciente, mostrarall

def menu():
    while True:
        print("*********** Sistema de Gestión de Consultas Médicas ***********")
        print("1. Registrar paciente          ********************************")
        print("2. Anadir estado del paciente          ************************")
        print("3. Mostrar datos de un paciente        ************************")
        print("4. Mostrar a todos los pacientes       ************************")
        print("5. Salir                               ************************")
        opcion = int(input('Ingrese la opcion que necesita: '))

        if opcion == 1:
            regpaciente()
            print("************************************************************")
        elif opcion == 2:
            addestado()
            print("************************************************************")
        elif opcion == 3:
            mostrarpaciente()
            print("************************************************************")
        elif opcion == 4:
            mostrarall()
            print("************************************************************")
        elif opcion == 5:
            print("Fin del programa.")
            print("************************************************************")
        else:
            print("Opcion no valida, ingrese de nuevo recuerda usar las opciones del 1 al 6.")
            print("************************************************************")

if __name__ == "__main__":
    menu()