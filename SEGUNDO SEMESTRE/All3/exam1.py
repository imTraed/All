valor=[]
datos=int(input("Ingrese cuantos datos desea ingresar: "))

for i in range (datos):
    valores = int(input(f"Ingrese digito {i+1}: "))
    valor.append(valores)
resultado = sum(valor) / datos
varianza = sum((x - resultado) ** 2 for x in valor) / len(valor)

print(f"Los numeros ingresados fueron {valor}")
print(resultado)
print("La varianza es:", varianza)