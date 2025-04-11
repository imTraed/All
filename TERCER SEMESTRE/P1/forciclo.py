'''
for i in range(1,13):
    print("Tabla del" , i)
    for j in range (1,13):
        print (i, '*', j , "=",i*j)

for i in[0,10,2]:
    print("Hola" , i)

for i in [2,4,8]:
    print("el valor de" ,i,"y su cuadrado es",i**2 )

for i in ["Edison",20,"Ecuador",True]:
    print("El valor de i es:" , i)

for i in [1,2,3,4,5]:
    print("tabla del", i)
    for j in [1,2,3,4,5]:
        print(i,"*",j,"=",i*j)

'''

for i in range (1,11):
    if i % 2:
        print('El numero:')
        print(i,"es impar")
for j in range (1,11):
    if j % 2:
        print('El numero:')
    else:
        print(j,"es par")