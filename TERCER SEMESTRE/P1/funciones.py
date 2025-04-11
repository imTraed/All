print("funciones recursivas")
def cuenta_regresiva(numero):
    numero -=1
    if numero >0:
        print(numero)
        cuenta_regresiva(numero)
    else:
        print("booom!")
    print("fin de la funcion" , numero)
cuenta_regresiva(5)
print("\n")


