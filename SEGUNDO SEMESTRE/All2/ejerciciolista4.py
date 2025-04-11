productos = []
cantidades = []
precios_unitarios = []
while True:
    print("1.Ingreso de datos")
    print("2.Consulta de valores ingresados en inventario")
    print("3.Reporte total")
    print("4.salir")
    opcion = int(input("Seleccione una opcion: "))
#
    if opcion == 1: 
        producto = input("Ingrese el nombre del producto: ")
        cantidad = int(input(f"Ingrese la cantidad de {producto}: "))
        precio_unitario = float(input(f"Ingrese el precio unitario de {producto}: "))
        
        productos.append(producto)
        cantidades.append(cantidad)
        precios_unitarios.append(precio_unitario)
#
    elif opcion == 2:
        print("Sus valores en el inventario es:")
        
    elif opcion == 3:
        print("Reporte total")
        print(f"Los productos en la lista son: {productosadd}")
    elif opcion == 4:
        print("saliendo")
        break