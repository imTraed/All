class Pajaro:
    def sonido(self):
        print("El pájaro canta")

class Gato:
    def sonido(self):
        print("El gato maúlla")

def hacer_sonido(animal):
    animal.sonido()

mi_pajaro = Pajaro()
mi_gato = Gato()

hacer_sonido(mi_pajaro)  
hacer_sonido(mi_gato)