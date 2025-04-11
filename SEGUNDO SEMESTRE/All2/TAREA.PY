#a.	Realizar un programa que ingrese una cadena de caracteres 
# por teclado que representa una frase (palabras separadas por espacios), 
# el programa debe contar cuantas palabras tiene la frase.

texto = input("Introduce su texto: ")
num_texto = len(texto.split())
print("La frase tiene", num_texto, "palabras")

#b.	Realizar un programa que se ingrese una cadena de caracteres por 
# teclado que represente una frase (palabras separadas por espacios), 
# el programa debe presentar la inicial de la letra en mayúscula de cada palabra.
#print((texto.split()


texto = input("Introduce una cadena de caracteres: ")
iniciales = ''.join([palabra[0].upper() for palabra in texto.split()])
print("Iniciales:", iniciales)


#c.	Realizar un programa que se ingrese por teclado una cadena de caracteres 
# (palabra separada por espacio), realizar las siguientes instrucciones: 
#i.	Ingresar un carácter para buscar en la frase ingresada
#ii.	Ingresar un carácter para sustituir el carácter ingresado en le literal anterior
#iii.	Presentar la frase ingresada con el cambio del carácter nuevo 

buscar = (input("Ingrese su letra a buscar: "))
remplazar = (input("Ingrese su letra a remplazar: "))
print(texto.replace(buscar, remplazar))  

#d.	Realizar un programa que lea una cadena y un carácter por teclado 
# (validar que lo ingresado como carácter sea carácter alfanumérico) 
# y muestra cuantas veces aparece el carácter en la cadena.

texto = input("Introduce una cadena (frase a ingresar): ")
caracter = input("Introduce un caracter: ")
while not caracter.isalnum() or len(caracter) != 1:
    print("Por favor, introduce un solo caracter alfanumérico.")
    caracter = input("Introduce un caracter: ")
ocurrencias = texto.count(caracter)
print(f"En la cadena '{texto}' aparece {ocurrencias} veces el caracter '{caracter}'.")

#e.	Realizar un programa 
#que se ingrese una cadena por teclado sin tildes y 
#cuente cuantas consonantes tiene la cadena.

texto = input("Introduce un texto (sin tildes): ")
consonantes = "bcdfghjklmnpqrstvwxyzBCDFGHJKLMNPQRSTVWXYZ"
num_consonantes = sum(1 for letra in texto if letra in consonantes)
print("Número de consonantes:", num_consonantes)