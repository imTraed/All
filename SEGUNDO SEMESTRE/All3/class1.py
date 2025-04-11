Edad = []
Genero = []
Instruccion = []
Salario = []

personas = int(input("Ingrese la cantidad de personas que desea ingresar: "))
for i in range(personas):
    Edad1 = int(input("Ingrese su edad: "))
    while Edad1 <0:
        print("No puede ser la edad menor a 0")
    Edad.append(Edad1)

    while True:
        Genero1 = str(input(f"Elije tu genero escribiendo 'M' si es Masculino, 'F' si es femenino o 'O' si es Otro: ")).upper()
        if Genero1 == "M":
            Genero.append("Masculino")
            break
        elif Genero1 == "F":
            Genero.append("Femenino")
            break
        else:
            print("Elija del 1 al 3")

    while True:
        print("Elije tu instruccion: ")
        print("1.Primaria")
        print("2.Secundaria")
        print("3.Superior")
        Instruccion1 = int(input())
        if Instruccion1 == 1:
            Instruccion.append("Primaria")
            break
        elif Instruccion1 == 2:
            Instruccion.append("Secundaria")
            break
        elif Instruccion1 == 3:
            Instruccion.append("Superior")
            break
        else:
            print("Elija del 1 al 3")

    Salario1 = int(input("Ingrese su salario: "))
    while Salario1 <0:
        print("No puede ser la edad menor a 0")
    Salario.append(Salario1)

print(Edad, Genero, Instruccion, Salario , end="")

hombressalario = [Salario[i] for i in range (personas) if Genero[i] =="Masculino"]
mujeressalario = [Salario[i] for i in range (personas) if Genero[i] =="Femenino"]

total_hombres = 0
for salario in hombressalario:
    total_hombres += salario

total_mujeres = 0
for salario in mujeressalario:
    total_mujeres += salario

# Calcular promedios
promedio_hombres = total_hombres / len(hombressalario ) if hombressalario  else 0
promedio_mujeres = total_mujeres / len(mujeressalario) if mujeressalario else 0

print("\nResultados:")
print(f"Promedio de salario de hombres: {promedio_hombres:.2f}")
print(f"Promedio de salario de mujeres: {promedio_mujeres:.2f}")