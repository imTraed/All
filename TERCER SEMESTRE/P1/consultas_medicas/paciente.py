class Paciente:
    def __init__(self, nombre,cedula,edad,sangre):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        self.sangre = sangre
        self.estados = []

    def addestado(self, estado):
        self.estados.append (estado)

    def mostrardatos(self):
        print(f"Nombre: {self.nombre}")
        print(f"Cedula: {self.cedula}")
        print(f"Edad: {self.edad}")
        print(f"Tipo de sangre: {self.sangre}")