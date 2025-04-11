# Salir del programa.
class Persona:
    def __init__(self, nombre, edad, ocupacion):
        self.nombre = nombre
        self.edad = edad
        self.ocupacion = ocupacion

    def description(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Ocupación: {self.ocupacion}"

def mostrar_menu():
    print("\n--- Gestión de Personas ---")
    print("1. Agregar persona")
    print("2. Mostrar todas las personas")
    print("3. Buscar persona por nombre")
    print("4. Salir")
personas = []

while True:
    mostrar_menu()
    opcion = input("Seleccione una opción: ")
    if opcion == "1":
        nombre = input("Ingrese el nombre de la persona: ")
        edad = int(input("Ingrese la edad de la persona: "))
        ocupacion = input("Ingrese la ocupación de la persona: ")
        nueva_persona = Persona(nombre, edad, ocupacion)
        personas.append(nueva_persona)
        print(f"La persona '{nombre}' ha sido agregada.")
    elif opcion == "2":
        if len(personas) > 0:
            print("\n--- Lista de Personas ---")
            for persona in personas:
                print(persona.description())
        else:
            print("No hay personas en la lista.")
    elif opcion == "3":
        if len(personas) > 0:
            nombre_buscar = input("Ingrese el nombre de la persona a buscar: ")
            encontrada = False

            for persona in personas:
                if persona.nombre.lower() == nombre_buscar.lower():
                    print("Persona encontrada:")
                    print(persona.description())
                    encontrada = True
                    break

            if not encontrada:
                print(f"No se encontró a '{nombre_buscar}' en la lista.")

        else:
            print("No hay personas en la lista.")
    elif opcion == "4":
        print("¡Hasta luego!")
        break
    else:
        print("Opción no válida. Por favor, seleccione una opción válida.")