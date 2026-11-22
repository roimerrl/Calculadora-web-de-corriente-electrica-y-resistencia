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
    material = 
    longitud_ida = float(input(" Ingrese la distancia fuente-carga: ")) # Metros 
    seccion_transversal = float(input(" Ingrese el area del material conductor: ")) # mm ** 2

    return tension, resistencia_carga, material, longitud_ida, seccion_transversal

def validaciones():
    
def modelo_matematico():