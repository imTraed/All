"""matriz = [(1,2,3), (5,6,7)]
print(matriz)
print(matriz[1])
print(matriz[0][0])
"""

matriz = []
for i in range(3):
    fila=[]
    for j in range(3):
        print("fila" , i , "columna" , j)
        elemento = int(input("ingrese el valor"))
        fila.append(elemento)
    matriz.append(fila)
print(matriz)
""""
print("el producto de un esacalar por una matriz")
num = int(input("ingrese el valor del escalar: "))
producto = []
for f in range(3):
    fila = []
    for c in range (3):
        escalar = num*matriz[f][c]
        fila.append(escalar)
    producto.append(fila)

print(matriz)
print(producto)
print("--------------------------------------------------")
ressuma = []
for f in range(3):
    suma = []
    for c in range (3):
        resultadosuma = matriz[f][c] + producto[f][c]
        suma.append (ressuma)
    ressuma.append(suma)
print(ressuma)
        """