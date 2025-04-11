print("*************************************************")
print("Autores: Erick Moreno, Hugo Pineda, Joshua Jacome")
print("Fecha: 09/10/2024")
print("*************************************************")
'''
Ejercicio 1:
Se necesita un registro de la aprobacion o no de un estudiante de programacion
1. Aprueba el semestre si la suma: de los 4 parciales da un total de 30/50 y asiste al menos el 80% de clases
2. Si la asistencia es menor  al 80% aprueba con 40/50
3. Cada semana se asiste 4 veces a clases
4. El semestre dura 20 semanas
'''

print("Registro de aprobacion")
print("Nota primer parcial")
primer_parcial=int(input())
print("Nota segundo parcial")
segundo_parcial=int(input())
print("Nota tercer parcial")
tercer_parcial=int(input())
print("Nota cuarto parcial")
cuarto_parcial=int(input())

print("Ingrese las asistencias totales en el semestre")
asistencia_total=int(input())

aprobacion_semestre = primer_parcial + segundo_parcial + tercer_parcial + cuarto_parcial
promedio_semestre = aprobacion_semestre/4
asistencia_fin = 0.8*asistencia_total


if aprobacion_semestre >= 30:
    print("Aprobo el semestre")
    print("la nota es", promedio_semestre )
    print("****************************")
else:
    print("Reprobo el semestre")
    print("la nota es", promedio_semestre )
if asistencia_fin >= 64:
    print("Aprobo la asistencia" ,  asistencia_fin ,"%")
else:
    print("Reprobo la asistencia con: " , asistencia_fin ,"%")


