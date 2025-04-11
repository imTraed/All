print("Nombre: Joshua Jacome")
print("Fecha: 18/11/2024")
print("*********************")
#Se nececita ingressar 2 notas del 0 al 15 de n estudiantes pida el 
#nombre y calcular el promedio de cada estudiante (usar listas)
#el resultado es fredy nota1= 15  nota2= 0  promedio= 7.5
# Inicializamos listas para guardar los datos
nombres = []
notas1 = []
notas2 = []
promedios = []

# Pedir cuántos estudiantes se van a procesar
n = int(input("¿Cuántos estudiantes deseas ingresar? "))

# Usar un ciclo para registrar datos de cada estudiante
for i in range(n):
    print(f"\nEstudiante {i + 1}:")
    
    # Pedir el nombre del estudiante
    nombre = input("Ingresa el nombre del estudiante: ")
    nombres.append(nombre)
    
    # Pedir las dos notas, asegurándose de que estén entre 0 y 15
    nota1 = float(input("Ingresa la primera nota (0 a 15): "))
    while nota1 < 0 or nota1 > 15:
        print("Nota fuera de rango. Intenta nuevamente.")
        nota1 = float(input("Ingresa la primera nota (0 a 15): "))
    notas1.append(nota1)
    
    nota2 = float(input("Ingresa la segunda nota (0 a 15): "))
    while nota2 < 0 or nota2 > 15:
        print("Nota fuera de rango. Intenta nuevamente.")
        nota2 = float(input("Ingresa la segunda nota (0 a 15): "))
    notas2.append(nota2)
    
    # Calcular el promedio y guardarlo
    promedio = (nota1 + nota2) / 2
    promedios.append(promedio)

# Mostrar resultados
print("\nResultados:")
for i in range(n):
    print(f"{nombres[i]} - Nota1 = {notas1[i]}, Nota2 = {notas2[i]}, Promedio = {promedios[i]:.2f}")
