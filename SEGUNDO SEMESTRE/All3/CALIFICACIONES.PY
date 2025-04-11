listaestudiantes = []
notas1=[]
notas2=[]
notas3=[]
notas4=[]

def numest():
    numestudiantes=int(input("Ingrese el numero de estudiantes: "))
    for i in range (numestudiantes):
        estudiante = input("Ingrese al estudiante: ")
        nota1 = int(input("Ingrese la primera nota: " ))
        while nota1 < 0 or nota1 > 50:
            print("Error, escribe una nota mayor a 0 o menor a 50")
            nota1 = int(input("Ingrese nuevamente la primera nota: "))
        nota2 = int(input("Ingrese la segunda nota: " ))
        while nota2 < 0 or nota2 > 50:
            print("Error, escribe una nota mayor a 0 o menor a 50")
            nota2 = int(input("Ingrese nuevamente la segunda nota: "))
        nota3 = int(input("Ingrese la tercera nota: " ))
        while nota3 < 0 or nota3 > 50:
            print("Error, escribe una nota mayor a 0 o menor a 50")
            nota3 = int(input("Ingrese nuevamente la tercera nota: "))
        nota4 = int(input("Ingrese la cuarta nota: " ))
        while nota4 < 0 or nota4 > 50:
            print("Error, escribe una nota mayor a 0 o menor a 50")
            nota4 = int(input("Ingrese nuevamente la segunda nota: "))
        listaestudiantes.append (estudiante)
        notas1.append(nota1)
        notas2.append(nota2)
        notas3.append(nota3)
        notas4.append(nota4)


""""
while True:
    print("1. Reporte de estudiantes notas, promedio,estado")
    print("2. Promedio del curso")
    print("3. Mejor estudiante")
    print("4. Salir")
"""
numest()

print(listaestudiantes, notas1, notas2 ,notas3 , notas4)