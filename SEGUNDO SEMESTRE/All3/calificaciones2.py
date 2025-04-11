
def determinar_estado(promedio):
    if promedio >= 40:
        return "Aprobado"
    elif promedio >= 31:
        return "Suspenso"
    else:
        return "Reprobado"


def pedir_nota(nombre, parcial):
    while True:
        try:
            nota = float(input(f"Ingrese {parcial} (0-50) para {nombre}: "))
            if 0 <= nota <= 50:
                return nota
            else:
                print("La nota debe estar entre 0 y 50.")
        except ValueError:
            print("Por favor, ingrese un número válido.")


def ingresar_datos():
    estudiantes = []
    n = int(input("Ingrese la cantidad de estudiantes: "))

    for i in range(n):
        print(f"\nEstudiante {i+1}:")
        nombre = input("Nombre del estudiante: ")
        nota1 = pedir_nota(nombre, "Nota 1 (P1 /50)")
        nota2 = pedir_nota(nombre, "Nota 2 (P2 /50)")
        nota3 = pedir_nota(nombre, "Nota 3 (P3 /50)")
        nota4 = pedir_nota(nombre, "Nota Final (P4 /50)")


        promedio = (nota1 + nota2 + nota3 + nota4) / 4
        estado = determinar_estado(promedio)


        estudiantes.append({
            "nombre": nombre,
            "promedio": promedio,
            "estado": estado
        })
    return estudiantes


def mostrar_reporte(estudiantes):
    print("\n--- Reporte de Estudiantes ---")
    print(f"{'Nombre':<20} {'Promedio':<10} {'Estado':<10}")
    print("-" * 40)
    for est in estudiantes:
        print(f"{est['nombre']:<20} {est['promedio']:<10.2f} {est['estado']:<10}")


    suma_promedios = sum(est['promedio'] for est in estudiantes)
    promedio_curso = suma_promedios / len(estudiantes)
    print(f"\nPromedio del curso: {promedio_curso:.2f}")

    mejor = obtener_mejor_estudiante(estudiantes)
    print(f"Mejor estudiante: {mejor['nombre']} con un promedio de {mejor['promedio']:.2f}")


def obtener_mejor_estudiante(estudiantes):
    mejor_estudiante = estudiantes[0]
    for estudiante in estudiantes:
        if estudiante['promedio'] > mejor_estudiante['promedio']:
            mejor_estudiante = estudiante
    return mejor_estudiante


estudiantes = ingresar_datos()

mostrar_reporte(estudiantes)


def obtener_promedio(estudiante):
    return estudiante['promedio']