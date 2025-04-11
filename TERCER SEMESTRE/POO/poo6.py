class F1():
    def __init__(self,equipo,patrocinador):
        self.equipo = equipo
        self.patrocinador = patrocinador

class Redbull(F1):
    def corredores(self):
        return '{} al team lo patrocina {}'.format(self.equipo, self.patrocinador)

#return indica el final de la función pero también el valor que devuelve la función.

#La propiedad .format de un objeto Variable 
#obtiene o establece el formato de visualización de una variable.

ftop = Redbull(input("ingrese el team: ") , input("ingrese el patrocinador: "))
print(ftop.corredores())