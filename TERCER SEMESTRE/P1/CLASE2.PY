class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre 
        self.edad = edad 
        self.ocupacion = ocupacion 

    def descripcion(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupación: {self.ocupacion}"

nombres= []
edades = []
ocupaciones = []
#atributo son los datos o propiedades del objeto
#metodo son acciones que se pueden realizar 
while True:

    print("Menu")
    print("1. si desea ingresar personas")
    print("2. salir")
    menu = int(input("elija su opcion: "))

    if menu > 1 or menu <1:
        print("se cerro el programa")
        break

    elif menu == 1:
        num = int(input("ingrese el numero de personas que desea ingresar: "))
        for i in range(num):
            nombre = input(f"Ingrese el nombre de persona {i+1}: ")
            nombres.append (nombre)
            edad = int(input(f"Ingrese la edad de persona {i+1}: "))
            edades.append (edad)
            ocupacion =  input(f"Ingrese la ocupacion de persona {i+1}: ")
            ocupaciones.append (ocupacion)
            

    persona1 = Persona(nombres, edades, ocupaciones)
    print(persona1.descripcion())

