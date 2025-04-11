import random
from datetime import datetime, date, time
datfecha= []
datnombre = []
datpeso = []
dataltura = []
ejerciciostotales = []
tiempostotales = []
suma = 0
rutinaseleccionada = []  
frasesmotivacionales = ["EL DOLOR ES TEMPORAL, EL ORGULLO ES PARA SIEMPRE.",
"HOY ES EL DÍA PARA SUPERAR TUS LÍMITES.",
"EL ESFUERZO DE HOY SERÁ TU FUERZA DE MAÑANA.",
"NO PARES CUANDO ESTÉS CANSADO, PARA CUANDO HAYAS TERMINADO.",
"LOS RESULTADOS NO VIENEN FÁCIL, PERO SÍ VALEN LA PENA.",
"CADA REPETICIÓN CUENTA, NO DESPERDICIES NINGUNA.",
"TRANSFORMA EL ESFUERZO EN ENERGÍA Y LA ENERGÍA EN ÉXITO.",
"ERES MÁS FUERTE DE LO QUE PIENSAS.",
"LO DIFÍCIL ES LO QUE VALE LA PENA.",
"LA DISCIPLINA VENCE A LA MOTIVACIÓN TODOS LOS DÍAS."]

fecha= date.today()
datfecha.append(fecha)

def inicio ():
    print(f"""**************************************************
*                                                *
            {datnombre[0].upper()} AQUI COMIENZA TU PRIME           
*                                                *
**************************************************""")
    print( random.choice(frasesmotivacionales))
    print("**************************************************")
    print("SI ESTAS LISTO PARA COMENZAR")
    input("Presione enter  para continuar")

def datos():
    print("************************************************************************")
    print(f"""                        BIENVENIDO A STRONGLIFT                         
                                {fecha}                           
                    EL DIA QUE COMIENZA TU VICTORIA""")
    print("************************************************************************")
    print(f''' A CONTINUACION TE PEDIREMOS DATOS PARA UN ENTRENAMIENTO PERSONALIZADO
        Y DAR EL MEJOR RENDIMIENTO PARA TUS RESULTADOS ''')
    print("************************************************************************")
    nombre  = input("INGRESA TU NOMBRE: ")
    datnombre.append(nombre)
    peso = float(input('INGRESA TU PESO EN KG: '))
    datpeso.append(peso)
    altura = float(input('INGRESA TU ALTURA: '))
    dataltura.append(altura)

def recomendaciones():
    print("""
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        >>            RECOMENDACIONES          <<
        >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
        """)
    print("")
    print("***Mantente hidratado durante la session de ejercicios***")
    print("***Antes de empezar el entrenamiento , asegurate de realizar un calentamiento adecuado***")
    print("***Manten en cuenta que para porder mejorar debes realizar progresion en tus pesos , subiendolos cada semana*** ")
    print("***Al final de cada entrenamiento procura realizar un estiramiendo de 5 a 10 minutos***")
    input("Lea las recomendaciones , Presione enter  para continuar....")

def rutinas():
    print(">>>>>>>>>> RUTINAS <<<<<<<<<<")
    print(">>DURACION ESTIMADA 2 HORAS<<")
    print("1. Piernas y Glúteos")
    print("2. Biceps y Espalda")
    print("3. Hombros completo y Abdominales")
    print("4. Pecho y triceps")
    print("5. Femoral y cardio")
    print("6. Volver al menu principal: ")
    while True:
        opcion = input("Seleccione una opción: ")
        if len(opcion) == 1 and "1" <= opcion <= "6":  
            opcion = int(opcion)
            break
        else :
            print("INGRESE UNA OPCION VALIDA DE 1 A 6 : ")
            
    if opcion==1:
        rutinaseleccionada = [
            "Peso muerto convencional: 4x6-8",
            "Buenos días (good mornings): 4x10-12",
            "Puente de glúteos (en suelo): 3x12-15",
            "Paso al cajón con mancuerna: 3x12-14 por pierna",
            "Curl femoral (en máquina): 4x12-15",
            "Cardio HIT: 15-20 min (ej. 30 seg alta intensidad / 1 min descanso)"       
        ]
    
    elif opcion==2:
        rutinaseleccionada = [
            "Dominadas (o jalón al pecho): 4x8-10",
            "Remo con barra: 4x10-12",
            "Remo con mancuerna (unilateral): 3x12-14 por brazo",
            "Pull-over con mancuerna: 3x12-15",
            "Curl con barra: 3x10-12",
            "Curl martillo (con mancuerna): 3x12-14"
        ]
    elif opcion==3:
        rutinaseleccionada = [
            "Press militar con barra/mancuernas: 4x8-10",
            "Elevaciones laterales: 3x12-15",
            "Elevaciones posteriores (inclinado): 4x10-12",
            "Face pulls (con cable): 3x12-15",
            "Plancha abdominal: 3x30-60 segundos",
            "Ab wheel (rueda abdominal): 3x15-20",
            "Crunches en máquina o suelo: 4x20"
        ]
    elif opcion==4:   
        rutinaseleccionada =[
            "Press de banca plano: 4x8-10",
            "Press inclinado con mancuernas: 4x10-12",
            "Aperturas con mancuerna (plano/inclinado): 3x12-15",
            "Fondos en paralelas (para pecho): 3x10-12",
            "Press cerrado (con barra): 3x10-12",
            "Extensión de tríceps (cuerda o barra): 3x12-15"
        ]
    elif opcion==5:
        rutinaseleccionada = [
            "Peso muerto convencional: 4x6-8",
            "Buenos días (good mornings): 4x10-12",
            "Puente de glúteos (en suelo): 3x12-15",
            "Paso al cajón con mancuerna: 3x12-14 por pierna",
            "Curl femoral (en máquina): 4x12-15",
            "Cardio HIT: 15-20 min (ej. 30 seg alta intensidad / 1 min descanso)"
        ]
        
    elif opcion==6:
        print("Volviendo al menu principal")  
        
    print("\n--- Rutina Seleccionada ---")
    
    for ejercicio in rutinaseleccionada:
        
        print(f" {ejercicio}")
    input("Presione enter  para continuar.....")
        


while True:     
    datos()
    inicio()
    print("")
    print(">>>>>>>> STRONGLIFT TU CENTRO DE ACTIVIDAD FISICA <<<<<<<<<<")
    print("")
    print("1. SELECCIONA LA RUTINA QUE VAS A REALIZAR     <<<<<<<<<<<<<<<")
    print("2. REGISTRA TU ACTIVIDAD DE HOY     <<<<<<<<<<<<<<<<<<<<<<<<<<")
    print("3. ESTIMACION DE CALORIAS QUEMADAS     <<<<<<<<<<<<<<<<<<<<<<<")
    print("4. SALIR DEL PROGRAMA     <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<")
    opcionmenu = int(input("ELIJA SU OPCION: "))
    if opcionmenu == 1:
        recomendaciones()
        rutinas()
    elif opcionmenu == 2:
            ejercicio = input("Ingrese que ejericio realizo hoy: ")
            ejerciciostotales.append(ejercicio)
            tiempo= int(input("Cuantas tiempo realizo el ejercicio ingrese en enteros: "))
            tiempostotales.append(tiempo)
    elif opcionmenu == 3:
        for elemento in tiempostotales:
            suma += elemento 
        print(f"Los ejericios realizados fueron {ejerciciostotales} y {suma} el total de tiempo realizado ademas realizaste la siguiente rutina {rutinaseleccionada}")
        
        if rutinaseleccionada:
                print("\n--- Rutina que seleccionaste ---")
                for ejercicio in rutinaseleccionada:
                    
                    print(f"- {ejercicio}")
                    
                else:
                    print("No has seleccionado una rutina aún.")
    elif opcionmenu == 4:
        print("TE ESPERO DE VUELTA FAKIN BESTIA")
        break
