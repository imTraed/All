class libro:
    def __init__(self, Autor, anio, titulo):
        self.Autor = Autor 
        self.anio = anio 
        self.titulo = titulo 

    def descripcion(self):
        return f"Autor: {self.Autor}, anio: {self.anio}, titulo: {self.titulo}"

Autores= []
anios = []
titulos = []
#atributo son los datos o propiedades del objeto
#metodo son acciones que se pueden realizar 
while True:

    print("Menu")
    print("1. si desea ingresar varios libros")
    print("2. salir")
    menu = int(input("elija su opcion: "))

    if menu > 1 or menu <1:
        print("se cerro el programa")
        break

    elif menu == 1:
        num = int(input("ingrese el numero de libros que desea ingresar: "))
        for i in range(num):
            Autor = input(f"Ingrese el nombre del Autor {i+1}: ")
            Autores.append (Autor)
            anio = int(input(f"Ingrese el anio del libro {i+1}: "))
            anios.append (anio)
            titulo =  input(f"Ingrese el titulo del libro {i+1}: ")
            titulos.append (titulo)
            

    autor1 = libro(Autores, anio, titulo)
    print(autor1.descripcion())

