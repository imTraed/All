class Estudiante:
    def __init__(self, nombre , carrera , notafin):
        self.nombre = nombre
        self.carrera = carrera
        self.notafin = notafin

    def descripcion(self):
        return f"Nombre: {self.nombre}, Carrera: {self.carrera}, nota final: {self.notafin}"

while True:
    print("------------------------------------------------")
    print("MENU DE CALIFICACIONES")
    print("1.Ingresar datos")
    print("2.Salir")
    print("------------------------------------------------")
    opcion = int(input("Elije tu opcion: "))
    if opcion == 1:
        nombre = input("Ingrese el nombre del estudiante: ")
        carrera = input("Ingrese la carrera del estudiante: ")
        notafin = float(input("Ingrese la nota del estudiante: "))
        print("------------------------------------------------")

    elif opcion > 1 or opcion <1:
        print("se cerro el programa")
        break

    print("------------------------------------------------------------------------------------")
    estudiante1 = Estudiante(nombre, carrera, notafin)
    print(estudiante1.descripcion())
    print("------------------------------------------------------------------------------------")
    if notafin >= 7:
                print(f"------Aprobo con la calificacion de {notafin} ------")
    else:
                print(f"------ Reprobo con la calificacion de {notafin} ------")