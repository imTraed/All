from paciente import Paciente

pacientes = []

def regpaciente():
    print("************************************************************")
    nombre = input("Ingrese el nombre del paciente: ")
    cedula = int(input("Ingrese el numero de cedula: "))
    edad = int(input("Ingrese la edad: "))
    sangre = input("Ingrese el tipo de sangre: ")
    paciente = Paciente(nombre,cedula,edad,sangre)
    pacientes.append(paciente)
    print("************************************************************")

def buscpaciente(cedula):
    for pac in pacientes:
        if pac.cedula == cedula:
            return pac
    return None

def addestado():
    print("************************************************************")
    cedula = int(input("Ingrese la cedula del paciente: "))
    paciente = buscpaciente(cedula)
    print("************************************************************")
    if paciente:
        try:
            estado = input("Ingrese el estado del paciente: ")
            paciente.addestados(estado)
            print("El diagnostico del paciente fue agregado con exito.")
        except ValueError:
            print("Error al ingresar el diagnostico.")
    else:
        print("Paciente no encontrado.")

def mostrarpaciente():
    print("************************************************************")
    cedula = int(input("Ingrese la cedula del paciente: "))
    print("************************************************************")
    paciente = buscpaciente(cedula)
    if paciente:
        paciente.mostrardatos()
    else:
        print("************************************************************")
        print("Estudiante no encontrado.")

def mostrarall():
    if not pacientes:
        print("************************************************************")
        print("No existen pacientes registrados.")
    for pac in pacientes:
        pac.mostrardatos()