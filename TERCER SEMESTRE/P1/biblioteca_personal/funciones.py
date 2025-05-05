from libro import Libro
import datetime as dt
fecha = dt.date.today()
regbooks=[]

#REGISTRO NEW LIBRO
def regbook():
    titulo = input("Ingrese el titulo del libro que desea registrar: ")
    autor = input(f"Ingrese el autor de {titulo}: ")
    isbn = int(input(f"Ingrese el ISBN de {titulo}: "))
    genero = input(f"Ingrese el genero de {titulo}: ")
    regbook = Libro(titulo,autor,isbn,genero)
    regbooks.append(regbook)
    

#BUSQUEDA GENERAL LIBRO
def viewbook(isbn):
    for bok in regbooks:
        if bok.isbn == isbn:
            return bok
    return None

#PRESTAMO LIBRO
def prestbook():
    isbn = int(input("Ingrese el ISBN del libro que desea: "))
    book = viewbook(isbn)
    if book:
        try:
            print(f"El libro fue corractamente prestado la fecha es {fecha}.")
            regbooks.remove(book)
        except ValueError:
            print("Error al ingresar ISBN.")
    else:
        print("Libro no encontrado.")

#BUSQUEDA LIBRO
def viewallbooks():
    isbn = int(input("Ingrese ISBN del libro: "))
    libro = viewbook(isbn)
    if libro:
        libro.viewbook()
    else:
        print("Libro no encontrado.")

def allbook():
    if not regbooks:
        print("No existen libros registrados.")
    for bok in regbooks:
        bok.viewbook()