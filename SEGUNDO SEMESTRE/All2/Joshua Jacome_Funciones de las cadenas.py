# 1. capitalize()
frase = "joshua va a la universidad"
print(frase.capitalize()) 

# 2. swapcase()
frase = "Joshua va a la universidad"
print(frase.swapcase())  

# 3. replace()
frase = "Joshua va a la universidad"
print(frase.replace("a la universidad", "al karting")) 

# 4. find()
frase = "Joshua va a la universidad"
print(frase.find("universidad"))  

# 5. count()
frase = "Joshua va a la universidad y Joshua estudia mucho en la universidad"
print(frase.count("Joshua")) 
# 6. isalnum()
frase = "Joshua123vaalauniversidad"
print(frase.isalnum())  

# 7. isalpha()
frase = "Joshuavaalauniversidad"
print(frase.isalpha())  

# 8. strip()
frase = "Joshua va a la universidad"
print(frase.strip()) 

# 9. zfill()
frase = "Joshua va a la universidad"
print(frase.zfill(30)) 

# 10. join()
palabras = ["Joshua", "va", "a", "la", "universidad"]
print("$".join(palabras))

# 11. split()
frase = "Joshua va a la universidad"
print(frase.split()) 

# 12. String Formatting
nombre = "Joshua"
lugar = "universidad"
print(f"{nombre} va a la {lugar}") 
