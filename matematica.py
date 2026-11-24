from calculos import materiales

def modelo_matematico(tension, resistencia_carga, material, longitud_ida, seccion_transversal):
    # Llamamos a la funcion materiales()
    dic_materiales = materiales()
    resistividad = dic_materiales[material]
    
    # Se realizaran los calculos en el siguiente orden:
    conversion_area = seccion_transversal * 10 ** -6 # Para pasar de mm^2 a m^2
    longitud_total = longitud_ida * 2 
    resistencia_cable = (resistividad * longitud_total) / conversion_area # Ohmios
    resistencia_total = resistencia_carga + resistencia_cable # Ohmios
    corriente_estimada = tension / resistencia_total # Amperios
    caida_tension_cable = corriente_estimada * resistencia_cable # Voltios
    potencia_disipada = (corriente_estimada ** 2) * resistencia_cable # Wats

    # Devolvemos un diccionario para que Streamlit lo pueda leer facil
    return {
        "conversion_area": conversion_area,
        "longitud_total": longitud_total,
        "resistencia_cable": resistencia_cable,
        "resistencia_total": resistencia_total,
        "corriente_estimada": corriente_estimada,
        "caida_tension_cable": caida_tension_cable,
        "potencia_disipada": potencia_disipada
    }

