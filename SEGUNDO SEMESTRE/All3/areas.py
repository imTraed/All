def cuadrado():
    print("======================")
    print("=                    =")
    print("=                    =")
    print("=                    =")
    print("=                    =")
    print("=                    =")
    print("=                    =")
    print("=                    =")
    print("=                    =")
    print("=======================")
    NUM1 = float(input("ESCRIBE TU LADO: "))
    while NUM1 <0:
        print("Error, escribe un numero mayor a 0")
        NUM1 = float(input("ESCRIBE DE NUEVO TU LADO: ")) 
    print("88888888888888888888888888888888888888888888")
    print(f"El Area de tu cuadrado es:  {NUM1 * 4}")
    print("88888888888888888888888888888888888888888888")

def circulo():
    print("            ****             ")
    print("        ****    ****         ")
    print("    ****            ****      ")
    print("    ****            ****      ")
    print("    ****            ****      ")
    print("    ****            ****      ")
    print("    ****            ****      ")
    print("        ****    ****         ")
    print("            ****             ")
    Radio = float(input("ESCRIBE TU RADIO: "))
    while Radio <0:
        print("Error, escribe un numero mayor a 0")
        Radio = float(input("ESCRIBE DE NUEVO TU RADIO: "))
    print("88888888888888888888888888888888888888888888")
    print(f"El Area de tu circulo es:  {3.14 * Radio**2}")
    print("88888888888888888888888888888888888888888888")

def rectangulo():
    print("===========================")
    print("=                         =")
    print("=                         =")
    print("=                         =")
    print("=                         =")
    print("=                         =")
    print("=                         =")
    print("===========================")
    BASE = float(input("ESCRIBE TU BASE: "))
    while BASE <0:
        print("Error, escribe un numero mayor a 0")
        BASE = float(input("ESCRIBE DE NUEVO TU BASE: ")) 
    ALTURA = float(input("ESCRIBE TU ALTURA: "))
    while ALTURA <0:
        print("Error, escribe un numero mayor a 0")
        ALTURA = float(input("ESCRIBE DE NUEVO TU ALTURA: ")) 
    print("88888888888888888888888888888888888888888888")
    print(f"El Area de tu rectangulo es:  {BASE * ALTURA}")
    print("88888888888888888888888888888888888888888888")


while True:
    print("CALCULO DE AREAS")
    print("1.AREA DEL CUADRADO")
    print("2.AREA DEL CIRCULO")
    print("3. AREA  DEL RECTANGULO")
    print("4. SALIR")
    opcion = int(input("ELIJE LA OPCION QUE NECESITAS: "))
    if opcion == 1:
        cuadrado()
        input("Preione enter para continuar")
    elif opcion == 2:
        circulo()
        input("Preione enter para continuar")
    elif opcion == 3:
        rectangulo()
        input("Preione enter para continuar")
    elif opcion == 4:
        print("Gracias por usar el programa")
        break
    else:
        print('Opcion no valida')
