class Persona:
    def __init__(self,nombre,edad,ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion
    def descripcion(self):
        return f"Nombre:{self.nombre}, Edad: {self.edad} , ocupacion: {self.ocupacion}" 

nombre = input("Ingresa tu nombre: ")
edad = int(input("ingresa tu edad: "))
ocupacion = input("ingresa tu ocupacion: ")

nuevapersona = Persona(nombre,edad,ocupacion)
print("Info de la nueva persona")
print(nuevapersona.descripcion())