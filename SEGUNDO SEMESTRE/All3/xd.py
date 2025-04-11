def calcular_calorias(peso, duracion_min, met):
    """
    Calcula las calorías quemadas usando el MET.
    
    :param peso: Peso de la persona en kg.
    :param duracion_min: Duración de la actividad en minutos.
    :param met: Valor MET de la actividad.
    :return: Calorías quemadas.
    """
    duracion_horas = duracion_min / 60 
    return duracion_horas * peso * met

def main():
    peso = float(input("Ingresa tu peso en kg: "))
    duracion_min = float(input("Ingresa la duración de la actividad en minutos: "))
    
    met_correr = 8.0

    calorias_quemadas = calcular_calorias(peso, duracion_min, met_correr)
    
    print(f"Calorías quemadas al correr durante {duracion_min} minutos: {calorias_quemadas:.2f} kcal")

if __name__ == "__main__":
    main()