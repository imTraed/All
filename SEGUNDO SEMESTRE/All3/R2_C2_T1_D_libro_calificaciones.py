import numpy as np
DatoValido = True

LibroCalificaciones=np.empty((10, 2)).tolist()

#Lee Datos Materia y Calificacion y almacena en lista
i=0
while DatoValido==True:
    print ("Ingrese el nombre de la materia (ENTER para terminar)")
    Materia = input() 
    print("Ingrese la calificacion de la materia : ")
    Calificacion = input()
    
    if Materia != "":
        LibroCalificaciones[i][0] = Materia
        LibroCalificaciones[i][1] = int(Calificacion)
        i=i+1
    else:
        DatoValido = False

#Imprime Libro de calificaciones
print("MATERIA                    CALIFICACION")
print("-------                    ------------")
for j in range(i):
    print(LibroCalificaciones[j][0],"\t\t\t",LibroCalificaciones[j][1])

print ("\nAsignaturas a Repetir:")

for j in range(i):
    if LibroCalificaciones[j][1]< 7:
        print(LibroCalificaciones[j][0])
input()
