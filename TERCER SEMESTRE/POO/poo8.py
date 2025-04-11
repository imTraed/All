#Herencia Multiple
class Telefono:
    def __init__(self):
        pass
    def llamar(Self):
        print("Llamando...")
    def ocupado(self):
        print("Ocupado...")

class Camara:
    def __init__(self):
        pass
    def foto(self):
        print("Tomando foto...")

class Reproduccion:
    def __init__(self):
        pass
    def reproducciondemusica(self):
        print("reproduciendo musica...")
    def reproducirvideo(self):
        print("reproduciendo video...")

class smartphone(Telefono,Camara,Reproduccion):
    def __del__(self):
        print("Telefono apagado")

movil = smartphone()
print(movil.foto())
