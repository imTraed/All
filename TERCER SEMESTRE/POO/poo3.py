#metodos

class Calculadora:
    def __init__(self, val1 , val2):
        self.suma = val1 + val2
        self.resta = val1 - val2
        self.mult = val1 * val2
        self.div = val1 / val2
while True:
    print("Calculadora")
    print("1.Suma")
    print("2.Resta")
    print("3.Mult")
    print("4.Div")
    opcion = int(input("Ingrese su opcion que necesita: "))
    val1 = int(input("ingrese su valor 1: "))
    val2 = int(input("ingrese su valor 2: "))
    operacion = Calculadora(val1 , val2)
    if opcion == 1:
        print(operacion.suma)
    elif opcion == 2:
        print(operacion.resta)
    elif opcion == 3:
        print(operacion.mult)
    elif opcion == 4:
        print(operacion.div)
    else:
        print("Fin de programa")
        break