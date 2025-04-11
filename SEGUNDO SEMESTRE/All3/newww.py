# Definición de variables globales
datnombre = "joshua"
datpeso = 55.0
dataltura = 45.0
rutinaseleccionada = []

def seleccionar_rutina(opcion):
    global rutinaseleccionada
    if opcion == 5:
        rutinaseleccionada = [
            "Sprint en cinta o exterior: 10x30 seg alta intensidad",
            "Burpees: 5x15",
            "Saltos pliométricos: 4x12",
            "Cuerda para saltar: 10 minutos",
            "Carrera continua: 20 minutos (ritmo moderado)",
            "Mountain climbers: 4x30 seg"
        ]
    # Agrega más opciones según sea necesario
    # elif opcion == X:
    #     rutinaseleccionada = [...]

def guardaractividad():
    with open("ejercicios.txt", "w") as archivo:
        archivo.write("""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>           DATOS GUARDADOS          <<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
""")
        archivo.write("\n-------------------------------------------------------------------------------------\n")
        archivo.write(f"Nombre: {datnombre}\n")
        archivo.write(f"Peso: {datpeso}\n")
        archivo.write(f"Altura: {dataltura}\n")
        archivo.write("-------------------------------------------------------------------------------------\n")
        archivo.write("Rutina seleccionada:\n")
        for ejercicio in rutinaseleccionada:
            archivo.write(f"- {ejercicio}\n")
        archivo.write("-------------------------------------------------------------------------------------\n")
        archivo.write("\n")

def cargararchivos():
    print("ejercicios.txt")

# Ejemplo de uso
opcion = 5  # Esta sería la opción seleccionada por el usuario
seleccionar_rutina(opcion)
guardaractividad()