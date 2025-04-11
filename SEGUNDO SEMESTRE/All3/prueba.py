print("*************************************************")
print("Autores: Erick Moreno, Joshua Jacome")
print("*************************************************")
pesos=[]
alturas=[]
nombres=[]
apellidos=[]
edades=[]

def datos():
    numespacientess=int(input("Ingrese el numero de pacientes: "))
    for i in range (numespacientess):
        nombre= input("Ingrese el nombre: ")
        apellido = input("Ingrese el apellido: ")
        edad=int(input("Ingrese una edad entre 15 y 99 años: "))
        while edad < 15 or edad > 99:
            print("Error, escribe una edad entre 15 y 99 años: ")
            edad = int(input("Ingrese nuevamente la edad entre 15 y 99 años: "))
        peso=float(input("Ingrese el peso en kg o libras: "))
        while peso < 0:
            print("Error, escribe un peso mayor que 0: ")
            peso = float(input("Ingrese el peso en kg o libras mayor a 0: "))
        altura=float(input("Ingrese la altura: "))
        while altura < 0:
            print("Error, escribe una altura en metros o mayor que 0: ")
            altura = float(input("Ingrese su altura mayor a 0: "))
        pesos.append(peso)
        alturas.append(altura)
        nombres.append(nombre)
        apellidos.append(apellido)
        edades.append(edad)    
datos()
