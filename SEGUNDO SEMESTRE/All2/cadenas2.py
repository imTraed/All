print("Nombre: Joshua Jacome")
print("Fecha: 11/11/2024")
print("*********************")
#Capitalize
texto = "lorem ipsum dolor sit amet consectetur adipiscing"
print(texto.capitalize())

#Swapcase
texto_ejemplo="me GUSTA la PROGRAMACIÓN $1234"
texto_con_la_funcion=texto_ejemplo.swapcase()
print(texto_con_la_funcion)

#Replace
palabras = "Hola, como estan amigos?"
print(palabras)
print(palabras.replace("amigos", "amigos y amigas"))

#Find
localizar= "Esto es una prueba en clase"
imprimir=localizar.find("una")
print(imprimir)

#Count
frase="El perro es amigable y el perro es juguetón"
cantidad=frase.count("perro")
print(cantidad) 
numeros = [1, 2, 3, 4, 2, 5, 2]
apariciones_2 = numeros.count(2)
print(apariciones_2)

#Split
texto = input("Introduce una oración: ")
separacion = input("Introduce el carácter de separación para dividir la oración (por defecto es un espacio): ")
if separacion == "":
    partes = texto.split()  
else:
    partes = texto.split(separacion)
print("La oración dividida es:")
for i, parte in enumerate(partes):
    print(f"Parte {i+1}:{parte}")

#Join
lista_frutas = ["manzana", "banana", "pera"]
cadena_unida = ",".join(lista_frutas)
print(cadena_unida)

#Isalnum
print("")
print("\tIsalnum()")
print("Realizadao por: Javier Herrada y Gabriel Ramos")
print("")

while True:
    print("\nMenu de opciones:")
    print("1. Listas")
    print("2. Datos personales")
    print("3. Salir")
    opcion = input("Ingrese una opción: ")
    if opcion == "1":
        print("")
    print("\tLista True o False")
    texto = "pato,perro,mapache, Jose23,@Perez, Pepe,Jorgue45,777, 777 ,34#,20"

    for i in texto.split(","):
        R = i.isalnum()
    print(f"El nombre '{i}' es: {R}")


    if opcion == "2":
        print("Digitacion de su nombre y apellido")

    nombre = input("Digite su nombre: ")

    while not nombre.isalnum():
            print("El nombre no es válido. Debe contener solo letras.")
            nombre = input("Introduce un nombre válido: ")

    apellido = input("Digite su apellido: ")

    while not apellido.isalnum():
            print("El apellido no es válido. Debe contener solo letras.")
            apellido = input("Introduce un Apellido válido: ")

    print("El nombre es válido.")
    print(f"Su nombre es: {nombre} y su apellido es: {apellido}")


    if opcion =="3":
        print("Saliendo del programa.")
    break

#Isalpha
nombre1=("Christopher")
nombre2=("Christopher123")
nombre3=("Christopher Caiza")
print(nombre1.isalpha())
print(nombre2.isalpha())
print(nombre3.isalpha())

#strip
texto = "   Trabajo , Grupal!   "
texto_limpio = texto.strip()
print(f"Texto original: '{texto}'")
print(f"Texto limpio: '{texto_limpio}'")

#zfill
numero = "8"
nconceros = numero.zfill(4)
print(nconceros)

#String Formatting
nombre = input("Igrese su nombre: ")
ciudad = "Ambato"
precio = 105

carta = """
¡Hola, {0}!

Gracias por haber ingresado a mi pagina y realizar la compra. Es un gusto recibirte en nuestra pagina de ropa oficial de {1}.
Tu compra total fue de {2} $.

Gracias

""".format(nombre, ciudad, precio)


print(carta)