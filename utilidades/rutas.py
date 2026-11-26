from pathlib import Path

# Carpeta raíz del proyecto (la que contiene app.py)
RAIZ = Path(__file__).resolve().parent.parent

# Registro técnico de eventos (logs)
CARPETA_LOGS = RAIZ / "logs"
RUTA_LOG = CARPETA_LOGS / "app.log"

# Historial persistente de cálculos (JSON)
CARPETA_DATA = RAIZ / "data"
RUTA_HISTORIAL = CARPETA_DATA / "historial.json"

# Reportes exportados (CSV)
CARPETA_REPORTES = RAIZ / "reportes"

# Imágenes del proyecto (logo, portada y fotos del equipo)
RUTA_LOGO = RAIZ / "logo-2.png"
RUTA_IMG_CALCULADORA = RAIZ / "calculadora.png"
CARPETA_IMAGENES = RAIZ / "imagenes"
