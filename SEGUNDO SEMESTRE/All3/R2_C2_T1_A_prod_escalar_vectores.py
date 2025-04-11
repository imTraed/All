# Calculo de producto escalar de 2 vectores (arreglos)
arreglo1 = []
arreglo2 = []
prod_esc = 0.0

# Definimos un tamaño para las listas#
# Lo puedes cambiar si quieres#
tamanio = 3

print("Ingrese datos para el primer vector")
print("-----------------------------------")
# Leemos los datos y los agregamos a la lista
for i in range(tamanio):
    print("Ingrese dato componente ", end="")
    dato = int (input(i + 1))
    arreglo1.append(dato)
    
    print("Ingrese datos para el segundo vector")
for i in range(tamanio):
    print("-----------------------------------")
    print ("Ingrese dato componente ", end="")
    dato = int (input( i + 1))
    arreglo2.append(dato)

# Ahora mostremos las listas
print("Mostrando los datos del primer vector", i + 1)
for i in range(tamanio):
    print(" ",arreglo1[i])
print("Mostrando los datos del primer vector", i + 1)
for i in range(tamanio):
    print(" ",arreglo2[i])

#Calcula el producto escalar
for i in range(tamanio):
    prod_esc = prod_esc + (arreglo1[i] * arreglo2[i])
#Imprimer el producto escalar
print("El producto escalar de las listas ingresadas es:", prod_esc)
input()