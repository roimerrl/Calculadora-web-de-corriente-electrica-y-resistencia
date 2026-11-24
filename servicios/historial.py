import json
import os
import datetime

RUTA_JSON = "data/historial.json"

def guardar_calculo(entradas, resultados):
    # Si la carpeta data no existe, la creamos
    if not os.path.exists("data"):
        os.mkdir("data")

    # Leemos lo que ya hay
    historial = leer_historial()

    # Obtenemos la fecha actual como texto
    fecha_actual = str(datetime.datetime.now())

    # Creamos el nuevo registro
    registro = {
        "id": len(historial) + 1,
        "fecha": fecha_actual,
        "entradas": entradas,
        "resultados": resultados
    }
    
    # Lo agregamos a la lista
    historial.append(registro)

    # Guardamos el archivo
    archivo = open(RUTA_JSON, "w", encoding="utf-8")
    json.dump(historial, archivo, indent=4)
    archivo.close()
    
    return registro["id"]

def leer_historial():
    if not os.path.exists(RUTA_JSON):
        return []
        
    try:
        archivo = open(RUTA_JSON, "r", encoding="utf-8")
        datos = json.load(archivo)
        archivo.close()
        return datos
    except:
        # Si el archivo esta dañado, devolvemos una lista vacia
        return []