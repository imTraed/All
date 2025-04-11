print("Nombre: Joshua Jacome")
print("Fecha: 25/11/2024")
print("Eliminar materias aprobadas de una lista")
print("*********************")
materias=[]
notas=[]

for i in range (5):
    materia = input("ingrese la materia")
    materias.append(materia)
    nota = float(input(("ingrese la nota: ")))
    while nota <0 or nota >10:
        print("ingrese la nota entre 0 y 10")
        nota= float(input("ingrese la nota: "))
    notas.append(nota)

#imprimir listas
for i in range(5):
    print(f"en" , materias [i] , "obtuvo una nota de" , notas[i])
#eliminar materias aprobadas
i = 0 
while  i < len(notas):
    if notas[i] >= 7:
        del materias[i]
        del notas [i]
    else:
        i+=1
    print("Las materias reprobadas son: " , materias)
