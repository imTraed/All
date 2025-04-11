#funciones atributos

class Persona:
    edad = 27
    pais = "ecuador"
    nombre = 'josh'

doctor = Persona()

#getattr = se utiliza para obtener el valor de 
#un atributo de un objeto mediante el nombre del atributo
print(f'la edad es: {getattr(doctor, "edad")}') 

#hasattr() se puede utilizar para comprobar si un atributo 
#determinado pertenece a un objeto determinado. 
#Devuelve True si tiene el atributo y False en caso contrario.
print('el doctor tiene una edad?', hasattr(doctor,"edad"))

#Setattr es una función integrada de Python que se utiliza 
#para asignar o modificar los atributos de un objeto
print(f"el nombre anterior era: {doctor.nombre}")
setattr(doctor, "nombre", input("ingresa el nuevo nombre: "))
print(f"el nuevo nombre es: {doctor.nombre}")

#es un método integrado en Python que se utiliza 
#para eliminar el atributo nombrado del objeto.
delattr(Persona,"pais")
print(doctor.pais)