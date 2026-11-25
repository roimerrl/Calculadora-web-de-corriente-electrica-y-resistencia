import json
import os
import datetime
from servicios.logs import logger 

RUTA_JSON = "data/historial.json"

def guardar_calculo(entradas, resultados):
    # Si la carpeta data no existe, la creamos
    if not os.path.exists("data"):
        os.mkdir("data")

    # Leemos lo que ya hay
    historial = leer_historial()

    # Obtenemos la fecha actual como texto
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # formato id de 4 digitos
    nuevo_id = f"{len(historial) + 1:04d}"

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
    with open(RUTA_JSON, "w", encoding="utf-8") as archivo:
        json.dump(historial, archivo, indent=4, ensure_ascii=False)

    logger.info(f"Cálculo guardado exitosamente con ID: {nuevo_id}")
    return nuevo_id

def leer_historial():
    if not os.path.exists(RUTA_JSON):
        return []
        
    try:
        with open(RUTA_JSON, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        return datos
    
    except json.JSONDecodeError:
        # Si el archivo está dañado, devolvemos una lista vacía y avisamos
        logger.warning("El archivo historial.json está dañado. Se devuelve lista vacía.")
        return []
    
    except Exception as e:
        logger.error(f"Error al leer historial: {e}")
        return []