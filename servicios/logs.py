# Servicio de logs técnicos del sistema.
import logging
import re

from utilidades.rutas import CARPETA_LOGS, RUTA_LOG

# Nombre propio del logger (NO usar el logger raíz)
NOMBRE_LOGGER = "calculadora_web"


def configurar_logs():
    """Configura y devuelve el logger de la aplicación."""
    # Crear la carpeta logs/ si no existe
    CARPETA_LOGS.mkdir(parents=True, exist_ok=True)

    logger = logging.getLogger(NOMBRE_LOGGER)
    logger.setLevel(logging.INFO)
    logger.propagate = False  # no reenviar al logger raíz (evita duplicados)

    # Evitar duplicar handlers si el módulo se carga varias veces
    if not logger.handlers:
        archivo_handler = logging.FileHandler(
            RUTA_LOG, encoding="utf-8", delay=True
        )
        # Formato obligatorio: fecha | nivel | módulo.función | mensaje
        formato = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(module)s.%(funcName)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
        archivo_handler.setFormatter(formato)
        logger.addHandler(archivo_handler)

    return logger


logger = configurar_logs()

# ---------------------------------------------------------------------------
# Lectura de eventos para la página "Logs Técnicos"
# ---------------------------------------------------------------------------
# Formato que escribe así:
#   2026-11-25 10:00:00 | INFO | validaciones.validar_entradas | mensaje
PATRON_NUEVO = re.compile(
    r"^(\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2})\s*\|\s*"
    r"(INFO|WARNING|ERROR)\s*\|\s*([^|]+?)\s*\|\s*(.+)$"
)


def generar_eventos():
    """
    Generador (yield) que recorre app.log línea a línea y produce los
    eventos reconocidos como diccionarios:

        {"fecha": ..., "nivel": ..., "modulo": ..., "mensaje": ...}

    - Produce un evento a la vez con yield (no carga todo de golpe).
    - Ignora las líneas que no coinciden con el formato (líneas en
      blanco, trazados de excepciones de varias líneas, etc.).
    """
    if not RUTA_LOG.exists():
        return  # generador vacío: aún no hay archivo de logs

    try:
        with open(RUTA_LOG, "r", encoding="utf-8", errors="replace") as archivo:
            for linea in archivo:
                linea = linea.rstrip("\n\r")
                if not linea.strip():
                    continue

                coincidencia = PATRON_NUEVO.match(linea)
                if coincidencia:
                    fecha, nivel, modulo, mensaje = coincidencia.groups()
                    yield {
                        "fecha": fecha,
                        "nivel": nivel,
                        "modulo": modulo.strip(),
                        "mensaje": mensaje.strip(),
                    }
    except OSError as error:
        logger.error(f"Error al leer el archivo de logs: {error}")
