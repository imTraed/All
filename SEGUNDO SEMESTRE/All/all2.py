'''
Realice un programa que permita ingresar el nombre de una materia, 3 notas (entre 0 y 20) de
n estudiantes, calcule el promedio por estudiante, el promedio total de la materia.
Por estudiante se debe determinar si aprueba (con más de 15), si está suspenso (entre 10 y 15)
o si esta reprobado con menos de 10.
'''

print("Ingrese el nombre de la materia")
materia = input()
print("Ingrese las notas de los estudiantes no puede pasar de 20")
nota1 = int(input())
nota2 = int(input())
nota3 = int(input())

promedio = nota1  + nota2 + nota3 / 3
if promedio > 15:
    print(f"El estudiante aprueba con el promedio de {promedio}")
if promedio <= 15:
    print(f"Esta suspenso con el promedio de {promedio}")
    if promedio < 10:
        print(f"Esta reprobado con el promedio de {promedio}")
    else:
        print("Error")



