cont = 0
print("Ingrese su numero")
quatri = float(input())
while quatri <= 0:
    print("Ingrese su primer numero")
    quatri = float(input())
if quatri < 5000:
    cont += 1
quatri2 = float(input())
while quatri2 <= 0:
    print("Ingrese su segundo numero")
    quatri2 = float(input())
if quatri2 < 5000:
    cont += 1
quatri3 = float(input())
while quatri3 <= 0:
    print("Ingrese su tercer numero")
    quatri3 = float(input())
if quatri3 < 5000:
    cont += 1

if cont == 3:
    print("bueno")
elif cont ==2:
    print ("regular")
elif cont == 1:
    print("mala")
else:
    print("se paso de los 5000")

