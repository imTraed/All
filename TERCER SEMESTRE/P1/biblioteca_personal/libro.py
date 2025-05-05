class Libro:
#INICIALIZAR CLASE
    def __init__(self,titulo,autor,isbn,genero):
        self.titulo=titulo
        self.autor = autor
        self.isbn = isbn
        self.genero = genero
        self.listprest = []

#CREAR LISTA Y ANADIR
    def addlist(self, lista):
        self.listprest.append (lista)

#VISTA DE ALL ORDENADO
    def viewbook(self):
        print('***********************************************************')
        print(f"Titulo del libro : {self.titulo}")
        print(f"Autor: {self.autor}")
        print(f"ISBN: {self.isbn}")
        print(f"Genero : {self.genero}")
        print('***********************************************************')