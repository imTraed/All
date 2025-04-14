class Vehiculo:
    def mover(self):
        print("El vehículo se está moviendo")

class Auto(Vehiculo):
    def mover(self):
        print("El auto está moviéndose")

mi_auto = Auto()
mi_auto.mover() 