#Herencia
import math
class Calculadora:
    def __init__(self, numero):
        self.n = numero
        self.datos = [0 for i in range(numero)]

    def ingdatos(self):
        self.datos = [int(input(f"Ingrese su dato num {i+1} = ")) for i in range(self.n)]

class Operacionesbasicas(Calculadora):
    def __init__(self):
#Controlo los atributos
        Calculadora.__init__(self,2)
        
    def suma(self):
        a,b = self.datos
        sum = a+b
        print(f"El resultado es: {sum}")

    def resta(self):
        a,b = self.datos
        rest = a-b
        print(f"El resultado es: {rest}")

    def multipliacion(self):
        a,b = self.datos
        mult = a*b
        print(f"El resultado es: {mult}")

    def division(self):
        a,b = self.datos
        div = a/b
        print(f"El resultado es: {div}")

class raiz(Calculadora):
    def __init__(self):
        Calculadora.__init__(self, 1)
    
    def cuadrada(self):
        a = self.datos[0]
        print(f"El resultado es: {math.sqrt(a)}")


objeto = Operacionesbasicas()
#isinstance = Verificar la herencia si existe o no
print(isinstance(objeto,raiz))
#issubclass = verificar y revisar la herencia de la clase hijo pertenece a la padre
print(issubclass(Operacionesbasicas, Calculadora))

