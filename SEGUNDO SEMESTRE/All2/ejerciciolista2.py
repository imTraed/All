print("Nombre: Joshua Jacome")
print("Fecha: 25/11/2024")
print("Producto escalar por un vector")
print("*********************")

num = int(input("Ingrese el valor del escalar: "))
while num <= 0:
    print("solo se aceptan numeros mayores que 0")
    num=int(input("ingrese el valor del escalar"))

vector=[]
longitud = int(input("cuantos valores desea "))
while longitud<= 0:
    print("ingrese numeros mayores a 0")
    longitud = int(input("cuantos valores desea "))

for i in range (longitud):
    print("valor en la psicion" , i)
    valor=int(input("ingrese el valor del vector: "))
    vector.append(valor)

print(vector)
print("producto de un escalar por un vector")
producto = []
for i in range (longitud):
    multi= num * vector[i]
    producto.append(multi)
print(producto)