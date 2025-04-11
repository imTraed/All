print("*************************************************")
print("Autores: Erick Moreno, Hugo Pineda, Joshua Jacome")
print("*************************************************")


def crear_matriz(filas, columnas):
    matriz = []
    print("Ingrese los números de la matriz:")
    for i in range(filas):
        fila = []
        for j in range(columnas):
            elemento = float(input(f"Ingrese el número [{i+1},{j+1}]: "))  
            fila.append(elemento)
        matriz.append(fila)
    return matriz

def matriz_inferior(matriz):
    filas = len(matriz)
    columnas = len(matriz[0]) if filas > 0 else 0
    matriz_inferior = [[0] * columnas for _ in range(filas)]
    for i in range(filas):
        for j in range(columnas):
            if i >= j:
                matriz_inferior[i][j] = matriz[i][j]
    return matriz_inferior

def imprimir_matriz(matriz):
    for fila in matriz:
        print(" ".join(map(str, fila)))

def main():
    filas = int(input("Ingrese el número de filas: "))
    columnas = int(input("Ingrese el número de columnas: "))

    
    if filas != columnas:
        print("Error: El número de filas debe ser igual al número de columnas.")
        return

    if filas <= 0 or columnas <= 0:
        print("El número de filas y columnas debe ser mayor que 0.")
        return

    matriz = crear_matriz(filas, columnas)
    matriz_inf = matriz_inferior(matriz)
    print("Matriz inicial:")
    imprimir_matriz(matriz)
    print("Matriz inferior:")
    imprimir_matriz(matriz_inf)

if __name__ == "__main__":
    main()
