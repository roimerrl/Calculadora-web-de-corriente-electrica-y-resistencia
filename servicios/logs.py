import logging
import os

def configurar_logs():
    if not os.path.exists("logs"):
        os.mkdir("logs")

    # Configuracion basica de logs
    logging.basicConfig(
        filename="logs/app.log",
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger()

logger = configurar_logs()
