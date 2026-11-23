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
    seccion_transversal = float(input(" Ingrese el area del material conductor: ")) # mm^2

    return tension, resistencia_carga, material, resistividad, longitud_ida, seccion_transversal

def validaciones(tension, resistencia_carga, material,  longitud_ida, seccion_transversal):
     if tension <= 0:
     
     if resistencia_carga <= 0:

     if longitud_ida <= 0:

     if seccion_transversal <= 0:
     
     if material not in materiales:


def modelo_matematico(tension, resistencia_carga, resistividad, longitud_ida, seccion_transversal):
    # Se realizaran los calculos en el siguiente orden:
    conversion_area = seccion_transversal * 10 ** -6 # Para pasar de mm^2 a m^2
    longitud_total = longitud_ida * 2 
    resistencia_cable = (resistividad * longitud_total) / conversion_area
    resistencia_total = resistencia_carga + resistencia_cable
    corriente_estimada = tension / resistencia_total
    caida_tension_cable = corriente_estimada * resistencia_cable
    potencia_disipada = (corriente_estimada ** 2) * resistencia_cable 

    return conversion_area, longitud_total, resistencia_cable, resistencia_total, corriente_estimada, caida_tension_cable, potencia_disipada

dic_materiales = materiales()
parametros()