# Calculo de media y desviación estándar

import statistics

arreglo = []

#Recibe los datos sin condiciones
print("Ingrese datos para la lista (blanco para terminar)")
print("-------------------------------------------------")
# Leemos los datos
i=1 #contador
print("Ingrese dato ")
dat = input(1)
while dat != (""):
    dato=int(dat)
    arreglo.append(dato)
    print("Ingrese dato ")
    dat = input(i+1)

suma = 0.0;
for j in range(i):
    suma = suma + int(arreglo[j])

#Calcula la media estadística del grupo de datos almacenados en arreglo
media = statistics.mean(arreglo);

print ("La media de los números ingresados es: ", media);
#Calcula de desviación estándar del grupo de datos almacenados en arreglo    
destip = statistics.stdev(arreglo)
print("La desviación típica (estándar) es: ", destip)
input()