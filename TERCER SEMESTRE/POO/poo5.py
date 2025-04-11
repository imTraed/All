#metodo constructor
class Persona:
    pass
    def __init__(self, nombre, year):
        self.nombre = nombre
        self.years = year
    def descripcion(self):
        return '{} tiene {} years'.format(self.nombre, self.years)
    def comentario(self, frase):
        return '{} dice {} '.format(self.nombre,frase)

doctor = Persona("jose",25)
print(doctor.descripcion())
print(doctor.comentario("wow!"))

#modificar un atributo

class Email:
    def __init__(self):
        self.enviado = False
    def enviar_correo(self):
        self.enviado = True

mi_correo = Email()
print(mi_correo.enviado)
mi_correo.enviar_correo()
print(mi_correo.enviado)