import random
import time
from datetime import date
import matplotlib.pyplot as plt
import pygame

ejercicios = []
tiempos = []
datfecha = []
datnombre = []
datpeso = []
dataltura = []
ejerciciostotales = []
tiempostotales = []
rutinaseleccionada = []
carbohidratosquemados = []
frasesmotivacionales = [
    "EL DOLOR ES TEMPORAL, EL ORGULLO ES PARA SIEMPRE.",
    "HOY ES EL DÍA PARA SUPERAR TUS LÍMITES.",
    "EL ESFUERZO DE HOY SERÁ TU FUERZA DE MAÑANA.",
    "NO PARES CUANDO ESTÉS CANSADO, PARA CUANDO HAYAS TERMINADO.",
    "LOS RESULTADOS NO VIENEN FÁCIL, PERO SÍ VALEN LA PENA.",
    "CADA REPETICIÓN CUENTA, NO DESPERDICIES NINGUNA.",
    "TRANSFORMA EL ESFUERZO EN ENERGÍA Y LA ENERGÍA EN ÉXITO.",
    "ERES MÁS FUERTE DE LO QUE PIENSAS.",
    "LO DIFÍCIL ES LO QUE VALE LA PENA.",
    "LA DISCIPLINA VENCE A LA MOTIVACIÓN TODOS LOS DÍAS."
]


fecha = date.today()
datfecha.append(fecha)

def musica():
    """pygame.init()
    pygame.mixer.init()
    pygame.mixer.music.load("song.mp3") 
    pygame.mixer.music.play(-1)"""

def grafica():
    plt.plot(ejercicios, tiempos,)
    plt.xlabel("Ejercicios")
    plt.ylabel("Minutos")
    plt.title("Tiempo de ejercicio")
    plt.show()

def datos():
    print("************************************************************************")
    print(''' ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀       ⠀⠀⣀⡠⠤⠄⠐⠒⠒⠂⠠⠤⢀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⠒⠉⢀⡠⣀⣠⢤⠢⠂⢄⣀⠀⠀⠀⠉⠒⢄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⡠⠊⠡⠊⡀⡶⡁⠀⠄⠀⢀⡉⠙⠋⠋⢠⡙⢵⢄⠀⠀⠙⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⡞⠃⠀⠩⣰⢑⠢⢈⠀⡌⡶⠒⠒⠒⠤⠏⡥⡌⡲⡺⡦⡀⢇⠇⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⠃⡁⠪⣀⠤⠋⠘⢊⢔⣺⢌⢷⣋⠶⢄⠀⡇⠕⠫⠪⡊⣌⠮⣈⣂⠀⠱⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢠⡇⢀⠠⢀⢓⡂⡂⠀⠀⠉ ⠁⠁⣞⢠⣈⠎⡉⠚⡁⠀⡁⠆⠀⠊⠀⠒⠄⠀⢡⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣼⡇⣼⠢⣕⠑⠨⡇⠀⠀⠀⠀ ⠘⢌⢰⠉⠉⣉⢯⡥⠄⠀⠄⠐⢠⠸⠕⣸⠀⠈⣾⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣏⣗⡏⡄⠘⡑⠄⡚⠀⠀⠀⠀⠀⠀ ⠓⠀⠀⣁⠦⢥⢀⠀⣀⢐⣄⢢⠔⡠⡣⣀⡇⠑⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⡴⢇⢂⢄⠕⣼⠀         ⠀⡼⠯⣜⣢⢄⡘⠥⠖⡒⣛⡌⢗⡶⣿⠁⠀⢷⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣟⣽⢖⣓⠜⠧⡄⠀⠀⠀⠀⠀⢀⡔⠉⠉⠋⠘⢖⣻⡎⡗⡶⡵⠷⢶⣙⣾⡿⠀⠀⠹⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⣿⡿⡵⢏⢧⢆⣻⠝⡄⠀⢠⣖⡷⡄⡀⠀⠀⠀⢘⣊⡲⠿⢳⢪⣽⣿⣿⣿⡗⣸⠀⠇⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⢻⣿⣿⣽⣿⣾⣵⣶⣳⣴⣜⠛⠻⣷⣖⣄⠀⠀⢘⠿⢿⠯⠿⣾⣿⡿⠟⢻⢞⠿⢊⡴⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⠏⣼⠻⣿⣟⣿⣿⣾⣿⣿⣿⣿⣿⣿⡟⣿⠲⡤⣄⠌⢀⣠⡤⢶⠶⠉⠀⡤⠎⠁⣀⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠂⠀⣻⡄⠈⠻⢿⣿⣿⡿⣿⠿⣿⣿⣿⣿⣹⠨⣾⣻⡟⠅⠀⠒⣠⠐⠃⣘⡀⠔⠊⡜⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠀⠀⢙⣿⡤⡲⣶⡿⡟⡡⠀⠈⠁⠁⠰⠾⣿⠞⠃⠀⠀⠀⠤⢘⣞⠴⣿⣭⣿⠷⠊⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⠰⠀⢼⡿⣁⡁⠐⠀⣪⡜⡀⠀⡀⠀⠀⠀⣿⢀⠀⠀⢀⡠⡪⣾⣯⣶⣿⠠⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠸⡀⠉⠀⡀⠈⠹⠶⢾⢟⣿⣔⡄⣬⣆⢆⡠⡻⠿⠅⣈⢉⣠⡊⣿⠿⣿⠇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠒⠦⠦⠤⠤⠓⢿⢎⣥⣽⣿⣿⢛⠕⠒⣞⣄⢠⡌⠄⢢⣞⣀⡻⠂⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢶⣾⣿⣷⣱⠉⢀⣇⠀⠱⣎⣄⡺⣿⡯⠃⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⣏⡙⡁⠊⠉⡇⠉⠁⠺⢘⠯⡏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢯⣆⢠⡤⠊⢋⠀⠰⢼⠀⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢸⣿⣭⣤⡖⠀⠀⠠⣶⠀⣿⣷⡆⠀⠀''')
    print("************************************************************************")
    print("")
    print(f"""                        BIENVENIDO A STRONGLIFT                         
                                {fecha}                           
                    EL DIA QUE COMIENZA TU VICTORIA""")
    print("")
    print("************************************************************************")
    print("")
    print(f''' A continuacion te pediremos datos para un entrenamiento personalizado
        y dar el mejor rendimiento para tus resultados ''')
    print("")
    print("************************************************************************")
    print("")
    global datnombre, datpeso, dataltura
    
    while True:
        nombre = input("Ingresa tu nombre: ")
        if nombre == "":
            print("Ingrese su nombre. Intenta nuevamente.")
            
        elif nombre.isdigit():
            print("El nombre no puede ser un número. Intenta nuevamente.")
            
        else:
            datnombre.append(nombre)
            break
    while True:
        try:
            peso = float(input('Ingresa tu peso en kg: '))
            if peso <= 0:
                print("El peso debe ser un número positivo. Intenta nuevamente.")
            else:
                datpeso.append(peso)
                break
        except ValueError:
            print("Por favor, ingresa un número válido para el peso debe ser en kg.")
    while True:
        try:
            altura = float(input('Ingresa tu altura en cm: '))
            if altura <= 0:
                print("La altura debe ser un número positivo. Intenta nuevamente.")
            else:
                dataltura.append(altura)
                break
        except ValueError:
            print("Por favor, ingresa un número válido para la altura en cm.")
    
def inicio():
    print(f"""**************************************************
*                                                *
            {datnombre[0].upper()} AQUI COMIENZA TU PRIME           
*                                                *
**************************************************""")
    print("")
    print(f"   {random.choice(frasesmotivacionales)}")
    print("")
    print("**************************************************")
    print("")
    input("Si estas listo para comenzar presiona enter para continuar")

def recomendaciones():
    print("""
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        >>            RECOMENDACIONES         <<
        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """)
    print("***Mantente hidratado durante la sesión de ejercicios.***")
    print("---------------------------------------------------------")
    print("***Realiza un calentamiento adecuado antes de entrenar.***")
    print("---------------------------------------------------------")
    print("***Aumenta progresivamente los pesos para mejorar.***")
    print("---------------------------------------------------------")
    print("***Realiza estiramientos al finalizar el entrenamiento.***")
    print("")
    print("---------------------------------------------------------")
    print("ESTAS LISTO PARA EMPEZAR.... ")
    for i in range (8,0,-1):
        print(i,"....")
        time.sleep(1)
        
        
    
def rutinasperdergrasa():
    global rutinaseleccionada
    print("""
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        >>     RUTINAS PARA PERDER GRASA      <<
        >>     Duración estimada: 2 horas     <<
        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """)
    print("")
    print("1. Piernas y Glúteos")
    print("---------------------------------------------------------")
    print("2. Bíceps y Espalda")
    print("---------------------------------------------------------")
    print("3. Hombros completos y Abdominales")
    print("---------------------------------------------------------")
    print("4. Pecho y Tríceps")
    print("---------------------------------------------------------")
    print("5. Femoral y Cardio")
    print("---------------------------------------------------------")
    print("6. Volver al menú principal")
    print("---------------------------------------------------------")

    while True:
        opcion = input("Elije tu opción: ")
        if len(opcion) == 1 and "1" <= opcion <= "6":  
            opcion = int(opcion)
            break
        else:
            print("Ingrese una opción válida de 1 a 6: ")

    if opcion == 1:
        rutinaseleccionada = [
            "Sentadillas con barra: 4x10",
            "Peso muerto sumo: 4x12",
            "Zancadas con mancuernas: 3x12 por pierna",
            "Puente de glúteos con barra: 4x15",
            "Sentadilla con salto: 3x20",
            "Cardio HIT: 20 minutos (ej. 30 seg alta intensidad / 1 min descanso)"
        ]
        timpolist = 120
        ejerciciolist = "PERDER GRASA PIERNAS Y GLUTEOS"
        ejercicios.append(ejerciciolist)
        tiempos.append(timpolist)

    elif opcion == 2:
        rutinaseleccionada = [
            "Dominadas (o asistidas): 4x fallo",
            "Remo con barra: 4x10",
            "Remo con mancuerna unilateral: 3x12 por brazo",
            "Pull-over con mancuerna: 3x12",
            "Curl con barra: 3x10",
            "Curl martillo con mancuernas: 3x12"
        ]
        timpolist = 120
        ejerciciolist = "PERDER GRASA BÍCEPS Y ESPALDA"
        ejercicios.append(ejerciciolist)
        tiempos.append(timpolist)

    elif opcion == 3:
        rutinaseleccionada = [
            "Press militar con barra: 4x8",
            "Elevaciones laterales con mancuernas: 4x12",
            "Pájaro para deltoides posteriores: 3x15",
            "Face pulls con cable: 3x15",
            "Plancha abdominal: 3x1 min",
            "Mountain climbers: 3x30 seg"
        ]
        timpolist = 120
        ejerciciolist = "PERDER GRASA HOMBROS Y ABDOMINALES"
        ejercicios.append(ejerciciolist)
        tiempos.append(timpolist)

    elif opcion == 4:   
        rutinaseleccionada = [
            "Press de banca plano con barra: 4x8",
            "Press inclinado con mancuernas: 4x10",
            "Aperturas con mancuernas: 3x12",
            "Fondos en paralelas: 4x fallo",
            "Press cerrado con barra: 3x10",
            "Extensión de tríceps con cuerda: 3x12"
        ]
        timpolist = 120
        ejerciciolist = "PERDER GRASA PECHO Y TRÍCEPS"
        ejercicios.append(ejerciciolist)
        tiempos.append(timpolist)

    elif opcion == 5:
        rutinaseleccionada = [
            "Peso muerto rumano con barra: 4x10",
            "Curl femoral en máquina: 4x12",
            "Hip thrust con barra: 4x12",
            "Sprint en cinta: 10x30 seg alta intensidad",
            "Cuerda para saltar: 5 minutos",
            "Cardio HIT: 20 minutos"
        ]
        timpolist = 120
        ejerciciolist = "PERDER GRASA FEMORAL Y CARDIO"
        tiempos.append(timpolist)

    elif opcion == 6:
        print("Volviendo al menú principal")  
        return

    print("""
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        >>        RUTINA SELECCIONADA         <<
        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """)
    for ejercicio in rutinaseleccionada:  
        print(f" {ejercicio}")
    print("")
    input("Presiona enter para continuar")

def rutinasganarmusculo():
    global rutinaseleccionada
    print("""
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        >>     RUTINAS PARA GANAR MÚSCULO     <<
        >>     Duración estimada: 2 horas     <<
        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """)
    print("")
    print("1. Piernas y Glúteos")
    print("---------------------------------------------------------")
    print("2. Bíceps y Espalda")
    print("---------------------------------------------------------")
    print("3. Hombros completos y Abdominales")
    print("---------------------------------------------------------")
    print("4. Pecho y Tríceps")
    print("---------------------------------------------------------")
    print("5. Femoral y Cardio")
    print("---------------------------------------------------------")
    print("6. Volver al menú principal")
    print("---------------------------------------------------------")

    while True:
        opcion = input("Elije tu opción: ")
        if len(opcion) == 1 and "1" <= opcion <= "6":  
            opcion = int(opcion)
            break
        else:
            print("Ingrese una opción válida de 1 a 6: ")

    if opcion == 1:
        rutinaseleccionada = [
            "Sentadillas con barra: 5x8",
            "Prensa de piernas: 4x10",
            "Zancadas con barra: 4x12 por pierna",
            "Hip thrust con barra: 4x10",
            "Elevación de gemelos de pie: 4x15",
            "Extensión de piernas en máquina: 4x12"
        ]
        timpolist = 120
        ejerciciolist = "GANAR MÚSCULO PIERNAS Y GLUTEOS"
        ejercicios.append(ejerciciolist)
        tiempos.append(timpolist)

    elif opcion == 2:
        rutinaseleccionada = [
            "Dominadas lastradas: 4x6-8",
            "Remo con barra: 5x8",
            "Pull-ups (estricto): 4x fallo",
            "Remo con mancuerna: 4x10 por brazo",
            "Curl con barra Z: 4x10",
            "Curl martillo con mancuerna: 4x12"
        ]
        timpolist = 120
        ejerciciolist = "GANAR MÚSCULO BÍCEPS Y ESPALDA"
        ejercicios.append(ejerciciolist)
        tiempos.append(timpolist)

    elif opcion == 3:
        rutinaseleccionada = [
            "Press militar con barra: 4x8",
            "Elevaciones laterales pesadas: 4x12",
            "Face pulls con cable: 4x15",
            "Pájaro con mancuernas: 3x15",
            "Encogimientos para trapecio: 4x12",
            "Plancha abdominal con peso: 3x60 segundos"
        ]
        timpolist = 120
        ejerciciolist = "GANAR MÚSCULO HOMBROS Y ABDOMINALES"
        ejercicios.append(ejerciciolist)
        tiempos.append(timpolist)

    elif opcion == 4:   
        rutinaseleccionada = [
            "Press de banca plano pesado: 5x6",
            "Press inclinado con barra: 4x8",
            "Fondos en paralelas lastrados: 4x8",
            "Aperturas con mancuernas: 4x12",
            "Press cerrado para tríceps: 4x10",
            "Extensión de tríceps con cuerda: 4x12"
        ]
        timpolist = 120
        ejerciciolist = "GANAR MÚSCULO PECHO Y TRÍCEPS"
        ejercicios.append(ejerciciolist)
        tiempos.append(timpolist)

    elif opcion == 5:
        rutinaseleccionada = [
            "Peso muerto convencional: 5x6",
            "Prensa de piernas: 4x10",
            "Curl femoral en máquina: 4x12",
            "Zancadas con mancuerna: 4x12 por pierna",
            "Hip thrust con barra: 4x10",
            "Cardio moderado: 15 minutos (bicicleta o caminadora)"
        ]
        timpolist = 120
        ejerciciolist = "GANAR MÚSCULO FEMORAL Y CARDIO"
        ejercicios.append(ejerciciolist)
        tiempos.append(timpolist)

    elif opcion == 6:
        print("Volviendo al menú principal")  
        return

    print("""
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        >>        RUTINA SELECCIONADA         <<
        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """)
    for ejercicio in rutinaseleccionada:  
        print(f" {ejercicio}")
    print("")
    input("Presiona enter para continuar")

def rutinasmejorarresistencia():
    global rutinaseleccionada
    print("""
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        >>  RUTINAS PARA MEJORAR RESISTENCIA  <<
        >>    Duración estimada: 1.5 horas    <<
        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """)
    print("")
    print("1. Circuito Full Body")
    print("---------------------------------------------------------")
    print("2. Piernas y Cardio")
    print("---------------------------------------------------------")
    print("3. Upper Body Resistencia")
    print("---------------------------------------------------------")
    print("4. Core y Estabilidad")
    print("---------------------------------------------------------")
    print("5. HIIT y Sprints")
    print("---------------------------------------------------------")
    print("6. Volver al menú principal")
    print("---------------------------------------------------------")

    while True:
        opcion = input("Elije tu opción: ")
        if len(opcion) == 1 and "1" <= opcion <= "6":  
            opcion = int(opcion)
            break
        else:
            print("Ingrese una opción válida de 1 a 6: ")

    if opcion == 1:
        rutinaseleccionada = [
            "Burpees: 4x20",
            "Kettlebell swings: 4x15",
            "Push-ups: 4x20",
            "Sentadillas con salto: 4x15",
            "Mountain climbers: 4x30",
            "Cardio moderado: 10 min"
        ]
        timpolist = 110
        ejerciciolist = "MEJORAR RESISTENCIA CIRCUITO FULL BODY"
        ejercicios.append(ejerciciolist)
        tiempos.append(timpolist)

    elif opcion == 2:
        rutinaseleccionada = [
            "Zancadas con salto: 4x12",
            "Step-ups con mancuerna: 3x15 por pierna",
            "Peso muerto rumano ligero: 4x12",
            "Sprints en cinta: 8x30 seg alta intensidad",
            "Saltos a la caja: 4x12",
            "Cuerda para saltar: 5 minutos"
        ]
        timpolist = 110
        ejerciciolist = "MEJORAR RESISTENCIA PIERNAS Y CARDIO"
        ejercicios.append(ejerciciolist)
        tiempos.append(timpolist)

    elif opcion == 3:
        rutinaseleccionada = [
            "Push-ups con palmada: 3x15",
            "Dominadas asistidas rápidas: 4x fallo",
            "Press militar ligero: 4x12",
            "Fondos en paralelas rápidos: 4x12",
            "Flexiones diamante: 4x15",
            "Plancha dinámica: 3x1 min"
        ]
        timpolist = 110
        ejerciciolist = "MEJORAR RESISTENCIA UPPER BODY"
        ejercicios.append(ejerciciolist)
        tiempos.append(timpolist)

    elif opcion == 4:   
        rutinaseleccionada = [
            "Plancha con movimientos laterales: 3x30 seg",
            "Crunches bicicleta: 4x20",
            "Superman hold: 4x30 seg",
            "Ab wheel: 3x15",
            "Rotaciones con balón medicinal: 3x20",
            "Cuerda de batalla: 4x20 seg"
        ]
        timpolist = 110
        ejerciciolist = "MEJORAR RESISTENCIA CORE Y ESTABILIDAD"
        ejercicios.append(ejerciciolist)
        tiempos.append(timpolist)

    elif opcion == 5:
        rutinaseleccionada = [
            "Sprint en cinta o exterior: 10x30 seg alta intensidad",
            "Burpees: 5x15",
            "Saltos pliométricos: 4x12",
            "Cuerda para saltar: 10 minutos",
            "Carrera continua: 20 minutos (ritmo moderado)",
            "Mountain climbers: 4x30 seg"
        ]
        timpolist = 110
        ejerciciolist = "MEJORAR RESISTENCIA HIIT Y SPRINTS"
        ejercicios.append(ejerciciolist)
        tiempos.append(timpolist)

    elif opcion == 6:
        print("Volviendo al menú principal")  
        return

    print("""
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        >>        RUTINA SELECCIONADA         <<
        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """)
    for ejercicio in rutinaseleccionada:  
        print(f" {ejercicio}")
    print("")
    input("Presiona enter para continuar")

def mododerutina():
    print("""
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        >>   SELECCIONA EL TIPO DE OBJETIVO   <<
        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """)
    print("")
    print("1. Perder grasa")
    print("---------------------------------------------------------")
    print("2. Ganar musculo")
    print("---------------------------------------------------------")
    print("3. Mejorar resistencia")
    print("---------------------------------------------------------")
    opcionrutina = int(input("Elije tu opción: "))
    if opcionrutina == 1:
        rutinasperdergrasa()
    elif opcionrutina == 2:
        rutinasganarmusculo()  
    elif opcionrutina == 3:
        rutinasmejorarresistencia()  

def guardaractividad():
    global datnombre, datpeso, dataltura, rutinaseleccionada
    with open("ejercicios.txt", "w") as archivo:
        archivo.write("""
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
>>           DATOS GUARDADOS          <<
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
""")
        archivo.write("\n-------------------------------------------------------------------------------------\n")
        archivo.write(f"Nombre: {datnombre}\n")
        archivo.write(f"Peso: {datpeso}\n")
        archivo.write(f"Altura: {dataltura}\n")
        archivo.write("-------------------------------------------------------------------------------------\n")
        archivo.write("Rutina seleccionada:\n")
        for ejercicio in rutinaseleccionada:
            archivo.write(f"- {ejercicio}\n")
        archivo.write("-------------------------------------------------------------------------------------\n")
        archivo.write("\n")

musica()
datos()
inicio()

while True:
    print("""
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        >>              STRONGLIFT            <<
        >>   TU CENTRO DE ACTIVIDAD FISICA    <<
        <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
        """)
    print("")
    print("-------------------------------------------------------------------------------------")
    print("1. Selecciona la rutina que vas a realizar")
    print("-------------------------------------------------------------------------------------")
    print("2. Registra tu actividad veras tu estimacion de calorias quemadas y tu progreso")
    print("-------------------------------------------------------------------------------------")
    print("3. Guardar historial de actividades")
    print("-------------------------------------------------------------------------------------")
    print("4. Salir del programa")
    print("-------------------------------------------------------------------------------------")
    print("")
    
    
    while True:
        try:
            opcionmenu = int(input("Elije tu opción: "))
            if opcionmenu < 1 or opcionmenu > 4:
                print("Opción no válida. Ingresa un número entre 1 y 4.")
            else:
                break
        except ValueError:
            print("Por favor ingresa un número válido.")
    if opcionmenu == 1:
        recomendaciones()
        mododerutina()
    elif opcionmenu == 2:
        while True:
            ejercicio = input("Nombre del ejercicio (o escribe 'fin' para terminar): ")
        
            if ejercicio.lower() == 'fin':  
                print(f"Ejercicio '{ejercicio}' agregado correctamente.")
                break  # 
            elif ejercicio == "":  
                print("No se ingresó ningún ejercicio. Por favor, inténtalo nuevamente.")
            elif ejercicio.isdigit():  
                print("El nombre del ejercicio no puede ser un número. Intenta nuevamente.")
            else:  
                print(f"Ejercicio '{ejercicio}' agregado correctamente.")
                break 
        while True:
            try:
                tiempo = int(input(f"¿Cuántos minutos hiciste {ejercicio}? "))
                if tiempo <= 0:
                    print("El tiempo debe ser un número positivo. Intenta nuevamente.")
                else:
                    print(f"Registraste {tiempo} minutos para el ejercicio '{ejercicio}'.")
                    ejercicios.append(ejercicio)
                    tiempos.append(tiempo)
                    grafica()
                    break  
            except ValueError:
                print("Entrada no válida. Por favor, ingresa un número entero.")
    elif opcionmenu == 3:
        guardaractividad()
        print("")
        print("Historial guardado.")
        print("")

    elif opcionmenu == 4:
        print("TE ESPERO DE VUELTA, ¡FAKIN BESTIA!")
        break

