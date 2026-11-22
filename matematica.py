def materiales(): # Resistividades de los materiales
    materiales = {
        "cobre": 1.68 * 10 ** -6,
        "aluminio": 2.65 * 10 ** -8,
        "oro": 2.21 * 10 ** -8,
        "plata": 1.58 * 10 ** -8
        }
    
    return materiales

def parametros():
    tension = float(input(" Ingrese el voltaje DC suministrado por la fuente: ")) # Voltios
    resistencia_carga = float(input(" ingrese resistencia del dispositivo conectado: ")) # Ohmios
    material = input("Ingrese el material a utilizar (cobre, aluminio, oro, plata): ").lower() # Material que se va a utilizar
    resistividad = dic_materiales[material] # Resistividad del material llamando a la funcion materiales()
    longitud_ida = float(input(" Ingrese la distancia fuente-carga: ")) # Metros 
    seccion_transversal = float(input(" Ingrese el area del material conductor: ")) # mm ** 2

    return tension, resistencia_carga, material, resistividad, longitud_ida, seccion_transversal

dic_materiales = materiales()
parametros()

def validaciones():
    # Aca se evaluara por medio de ifs, try, except las variables de la funcion parametros
    # Si no cumple la evaluacion permitira cambiar el valor de lo que este dando el error
    # si cumple la evaluacion pasara a la siguiente funcion

def modelo_matematico():
    # Se realizaran los calculos en el siguiente orden y con las variables expresadas como:
    # conversion_area =
    # longitud_total =
    # resistencia_cable =
    # resistencia_total =
    # corriente_estimada =
    # caida_tension_cable =
    # potencia_disipada =
