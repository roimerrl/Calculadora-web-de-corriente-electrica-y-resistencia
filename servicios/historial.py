import json
from datetime import datetime

from servicios.logs import logger
from utilidades.rutas import CARPETA_DATA, RUTA_HISTORIAL


def guardar_calculo(entradas, resultados):
    """
    Guarda un cálculo exitoso en data/historial.json.

    - Importamos datetime con "from datetime import datetime" porque
      necesitamos la CLASE datetime, no el módulo completo.
    - El ID se calcula como el mayor de los existentes + 1, así no se
      repite aunque se borren registros del historial.
    - Si la escritura falla, se registra un ERROR en app.log y la
      excepción sube para que la interfaz la capture y muestre un mensaje.
    """
    # Si la carpeta data/ no existe, la creamos junto con el archivo
    CARPETA_DATA.mkdir(parents=True, exist_ok=True)

    # Leemos lo que ya hay guardado
    historial = leer_historial()

    # Obtenemos la fecha y hora actual como texto
    fecha_actual = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # ID nuevo: el mayor de los existentes + 1 (con formato de 4 dígitos)
    # int() convierte el id a numero aunque venga guardado como "0002"
    ids_existentes = [int(r.get("id", 0)) for r in historial if isinstance(r, dict)]
    siguiente_id = max(ids_existentes, default=0) + 1
    nuevo_id = f"{siguiente_id:04d}"  # :04d rellena con ceros hasta 4 digitos

    # Creamos el registro con id, fecha, entradas y resultados
    registro = {
        "id": nuevo_id,
        "fecha": fecha_actual,
        "entradas": entradas,
        "resultados": resultados
    }

    try:
        with open(RUTA_HISTORIAL, "w", encoding="utf-8") as archivo:
            json.dump(historial + [registro], archivo, indent=4, ensure_ascii=False)
    except OSError as error:
        logger.error(f"Error al escribir el historial JSON: {error}")
        raise  # la interfaz lo captura y muestra un mensaje claro

    logger.info(f"Cálculo guardado exitosamente con ID: {nuevo_id}")
    return nuevo_id


def leer_historial():
    """
    Lee el historial de cálculos desde data/historial.json.

    - Si el archivo todavía no existe, avisa con un WARNING y devuelve
      una lista vacía (primera vez que se usa la aplicación).
    - Si el JSON está dañado o ilegible, registra un ERROR y también
      devuelve una lista vacía para que la app no se cierre.
    - Si todo va bien, registra un INFO de lectura correcta.
    """
    if not RUTA_HISTORIAL.exists():
        logger.warning("El archivo historial.json aún no existe. Se devuelve una lista vacía.")
        return []

    try:
        with open(RUTA_HISTORIAL, "r", encoding="utf-8") as archivo:
            datos = json.load(archivo)
        logger.info(f"Historial leído correctamente ({len(datos)} cálculos).")
        return datos

    except json.JSONDecodeError:
        # JSON dañado o ilegible: registramos ERROR y continuamos con lista vacía
        logger.error("El archivo historial.json está dañado o ilegible. Se continúa con una lista vacía.")
        return []

    except OSError as error:
        logger.error(f"Error al leer el historial: {error}")
        return []
