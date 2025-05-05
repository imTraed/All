from funciones import regbook , prestbook , viewallbooks ,allbook

print('''
░░▒░░█░ 
░░▒░█ 
░░░█ 
░░█░░░░███████ 
░██░░░██▓▓███▓██▒ 
██░░░█▓▓▓▓▓▓▓█▓████ 
██░░██▓▓▓(◐)▓█▓█▓█ 
███▓▓▓█▓▓▓▓▓█▓█▓▓▓▓█ 
▀██▓▓█░██▓▓▓▓██▓▓▓▓▓█ 
░▀██▀░░█▓▓▓▓▓▓▓▓▓▓▓▓▓█ 
░░░░▒░░░█▓▓▓▓▓█▓▓▓▓▓▓█ 
░░░░▒░░░█▓▓▓▓█▓█▓▓▓▓▓█ 
░▒░░▒░░░█▓▓▓█▓▓▓█▓▓▓▓█ 
░▒░░▒░░░█▓▓▓█░░░█▓▓▓█ 
░▒░░▒░░██▓██░░░██▓▓██
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
▒▒▒BIBLIOTECA▒▒▒▒▒▒▒
▒▒▒▒▒▒VIRTUAL▒▒▒▒▒▒▒
▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒
''')

def menu():
    while True:
        print("")
        print("1. Registrar un nuevo libro            ************************")
        print("2. Registrar prestamo de un libro      ************************")
        print("3. Ver informacion de un libro         ************************")
        print("4. Mostrar libros disponibles          ************************")
        print("5. Salir                               ************************")
        opcion = int(input("Ingrese la opcion que desea: "))
        if opcion == 1:
            regbook()
        elif opcion == 2:
            prestbook()
        elif opcion == 3:
            viewallbooks()
        elif opcion == 4:
            allbook()
        elif opcion == 5:
            print("Fin del programa.")
            break
        else:
            print("Ingrese una opcion valida del 1 al 5.")

if __name__ == "__main__":
    menu()