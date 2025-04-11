cantidad = []
print("ingrese que cantidad de precios quiere ingresar")
cantidad = int(input())
for i in range (cantidad):
    precios = int(input(f"ingrese el valor {i+1} de sus precios: "))
    cantidad.append(precios)



    while True:
        print("1) Imprima los precios ingresados ")
        print("2) El promedio del precio del petróleo")
        print("3) ¿Cuál fue el día en el que estuvo más barato el barril de petróleo?")
        print("4) ¿Cuántos días el petróleo tuvo precios superiores al promedio?")
        print("5) Salir")
        opcion = int(input("Elija su opcion"))
        if opcion == 1:
            print(f"El precio es {precios}")
        
        if opcion == 5:
            break