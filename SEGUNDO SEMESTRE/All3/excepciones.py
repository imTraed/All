print(">>>>>>>>MANEJO DE EXCEPCIONES<<<<<<<<<")
print(">>>> Realizado por: Joshua Jacome <<<<")
print(">>>>>>>>>> Fecha: 9/12/2024 <<<<<<<<<<")
print("--------------------------------------")
print("*" * 25)
a=4
b=0

try:
    c=a/b
    print(f"La division es {c}")
    d=2+"2"
    print(f"La suma es {d}")
except ZeroDivisionError:
    print("No existe la division para 0")
except TypeError:
    print("Problema de tipos de datos")

try:
    c=5/0
    d=2+"Hola"
except Exception as ex:
    print(f"Ocurrio una excepcion{type(ex)}")
else:
    print("No a ocurrido excepcion")
finally:
    print("Ejecucion obligatoria")