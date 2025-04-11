import numpy as np

#Estructuras para almacenamiento

#Dim de la primera matriz n, m
#Dim de la segunda matriz k, l

n=2 #filas
m=3 #columnas

k=3 #filas
l=2 #columnas

#Lectura de matrices 
print("Ingrese datos para la primera matriz:")

#Inicializa repositorios tipo lista para matrices
matriz1=np.empty((n, m)).tolist()
matriz2=np.empty((k, l)).tolist()
i=0
while i<n:
   j=0
   while j<m:    
        print ("Ingrese dato componente ",i," ",j,": ",end=""),
        dato= input()
        matriz1[i][j] = int(dato)
        j=j+1
   i=i+1

print("\nIngrese datos para la primera matriz:")
i=0
while i<k:
   j=0
   while j<l:    
        print (f"Ingrese dato componente ",i," ",j,": ",end=""),
        dato= input()
        matriz2[i][j] = int(dato)
        j=j+1
   i=i+1


print("Imprimir Resultado:") 
print("El producto de multiplicar la primera por la segunda matriz ingresadas es")

#Calcula resultado de multiplicar matriz1 por matriz2
resultado= np.matmul(matriz1,matriz2)

#Imprime resultado de multiplicacion
for j in range(n):
    print(resultado[j])
input()