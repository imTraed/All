cont = 0
for i in range (0,3,1):
    quatri = float (input("Ingrese el valor del quatrimestre: "))
    while quatri < 0:
        quatri = float (input("Ingrese nurvmente el valor "))
    if quatri < 5000:
        cont += 1

if cont == 3:
    print("bueno")
elif cont ==2:
    print ("regular")
elif cont == 1:
    print("mala")
else:
    print("se paso de los 5000")

