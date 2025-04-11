cantidad_participantes = int(input("Ingrese el número de participantes: "))

nombres = []
calificaciones = []  
promedios_participantes = []  

for indice in range(1, cantidad_participantes + 1):
    print(f"\nParticipante {indice}:")
    
    nombre = input("Ingresa el nombre del estudiante: ")
    nombres.append(nombre)
    calificacion1 = float(input("Ingrese la primera calificación: "))
    calificacion2 = float(input("Ingrese la segunda calificación: "))
    
    calificaciones.append([calificacion1, calificacion2])

    promedio_participante = (calificacion1 + calificacion2) / 2
    promedios_participantes.append(promedio_participante) 
    print(f"El promedio del participante {indice} es: {promedio_participante:.2f}")

promedio_grupo = sum(promedios_participantes) / len(promedios_participantes)
print(f"\nEl promedio general del grupo es: {promedio_grupo:.2f}")
