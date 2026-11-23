def materiales(): # Resistividades de los materiales
    materiales = {
        "cobre": 1.68 * 10 ** -8,
        "aluminio": 2.65 * 10 ** -8,
        "oro": 2.21 * 10 ** -8,
        "plata": 1.58 * 10 ** -8
        }
    
    return materiales

def parametros(dic_materiales): # Es importante que en la calculadora se especifiquen las unidades
    tension = float(input(" Ingrese el voltaje DC suministrado por la fuente: ")) # Voltios
    resistencia_carga = float(input(" ingrese resistencia del dispositivo conectado: ")) # Ohmios
    material = input("Ingrese el material a utilizar (cobre, aluminio, oro, plata): ").lower() # Material que se va a utilizar
    resistividad = dic_materiales[material] # Resistividad del material llamando a la funcion materiales()
    longitud_ida = float(input(" Ingrese la distancia fuente-carga: ")) # Metros 
    seccion_transversal = float(input(" Ingrese el area del material conductor: ")) # mm^2

    return tension, resistencia_carga, material, resistividad, longitud_ida, seccion_transversal

def validaciones(tension, resistencia_carga, material,  longitud_ida, seccion_transversal):
     while tension <= 0:
         try:
             tension = float(input(" ERROR: La tension debe ser mayor a cero, ingrese un nuevo valor: "))
         except: ValueError
         print(" Debe ingresar un numero valido (Mayor a 0). ")

     while resistencia_carga <= 0:
         try:
                resistencia_carga = float(input(" ERROR: La resistencia de carga debe ser mayor a cero, ingrese un nuevo valor: "))
         except: ValueError
         print(" Debe ingresar un numero valido (Mayor a 0). ")

     while longitud_ida <= 0:
          try:
                longitud_ida = float(input(" ERROR: La longitud de ida debe ser mayor a cero, ingrese un nuevo valor: "))
          except: ValueError
          print (" Debe ingresar un numero valido (Mayor a 0). ")

     while seccion_transversal <= 0:
          try:
             seccion_transversal = float(input(" ERROR: La seccion transversal debe ser mayor a cero, ingrese un nuevo valor: "))
          except: ValueError
          print(" Debe ingresar un numero valido (Mayor a 0). ")
     
     while material not in dic_materiales:
        material = str(input(" El material que eligio no se encuentra en la lista (cobre, aluminio, oro, plata), ingrese un material valido ")).lower()

def modelo_matematico(tension, resistencia_carga, resistividad, longitud_ida, seccion_transversal):
    # Se realizaran los calculos en el siguiente orden:
    conversion_area = seccion_transversal * 10 ** -6 # Para pasar de mm^2 a m^2
    longitud_total = longitud_ida * 2 
    resistencia_cable = (resistividad * longitud_total) / conversion_area # Ohmios
    resistencia_total = resistencia_carga + resistencia_cable # Ohmios
    corriente_estimada = tension / resistencia_total # Amperios
    caida_tension_cable = corriente_estimada * resistencia_cable # Voltios
    potencia_disipada = (corriente_estimada ** 2) * resistencia_cable # Wats

    return conversion_area, longitud_total, resistencia_cable, resistencia_total, corriente_estimada, caida_tension_cable, potencia_disipada

dic_materiales = materiales()
tension, resistencia_carga, material, resistividad, longitud_ida, seccion_transversal  = parametros(dic_materiales)
modelo_matematico(tension, resistencia_carga, resistividad, longitud_ida, seccion_transversal)

# Se completo la prueba que el profe coloco para comprobar que el sistema funcione correctamente, 
# El modulo actualmente solo hace los calculos, mas no hace el print


