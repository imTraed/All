print("Nombre: Joshua Jacome")
print("Fecha: 11/11/2024")
print("*")

print("\nEjemplo de funciones de string:")
producto = "café en grano"
descripcion = "producto orgánico DE ALTA CALIDAD"
print("Producto:", producto)
print("1. Capitalize:", producto.capitalize())
print("2. Upper:", producto.upper())
print("3. Lower:", descripcion.lower())
print("4. Title:", descripcion.title())
print("5. Reemplazo de palabras:", descripcion.replace("ALTA CALIDAD", "excelente calidad"))

productos = []
precios = []

while True:
    print("\n--- Menú de Opciones ---")
    print("1. Ingresar producto")
    print("2. Registrar precios")
    print("3. Total de ventas")
    print("4. Salir")
    opcion = input("Seleccione una opción: ")

    if opcion == "1":
        producto = input("Ingrese el nombre del producto: ").title()
        descripcion = input("Ingrese una breve descripción: ").capitalize()
        productos.append((producto, descripcion))
        print(f"Producto guardado: {producto} - {descripcion}")



    promediodia1 = sum(temperaturas1) / len(temperaturas1)
    promediodia2 = sum(temperaturas2) / len(temperaturas2)
    promediodia3 = sum(temperaturas3) / len(temperaturas3)
    print(f"Promedio del día 1: {promediodia1:.2f}")
    print(f"Promedio del día 2: {promediodia2:.2f}")
    print(f"Promedio del día 3: {promediodia3:.2f}")



    elif opcion == "2":
        if not productos:
            print("Primero debe ingresar productos en la opción 1.")
        else:
            for i, (producto, descripcion) in enumerate(productos):
                while True:
                    try:
                        precio = float(input(f"Ingrese el precio para {producto}: "))
                        if precio >= 0:
                            precios.append(precio)
                            break
                        else:
                            print("El precio debe ser un valor positivo.")
                    except ValueError:
                        print("Entrada inválida. Ingrese un número.")
            print("Precios registrados:", precios)

    elif opcion == "3":
        if not precios:
            print("No hay precios registrados. Ingrese precios en la opción 2.")
        else:
            total_ventas = sum(precios)
            print(f"El total de ventas es: ${total_ventas:.2f}")

    elif opcion == "4":
        print("Saliendo del programa.")
        break

    else:
        print("Opción inválida, intente de nuevo.")
