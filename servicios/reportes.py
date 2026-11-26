import csv

from servicios.logs import logger
from utilidades.rutas import CARPETA_REPORTES


def exportar_csv(historial):
    """
    Exporta el historial de cálculos a un archivo CSV y retorna la ruta
    del archivo creado, o None si algo falla.

    - Los encabezados incluyen las unidades de cada magnitud.
    - Se escribe con encoding "utf-8-sig" (con BOM) para que Excel abra
      correctamente los acentos, la Ω y el mm².
    - Si el historial está vacío, avisa con WARNING y no exporta nada.
    """
    if not historial:
        logger.warning("Se intentó exportar el CSV con el historial vacío.")
        return None

    # Crear la carpeta reportes/ si no existe
    CARPETA_REPORTES.mkdir(parents=True, exist_ok=True)
    ruta_csv = CARPETA_REPORTES / "reporte_calculos.csv"

    try:
        with open(ruta_csv, "w", newline="", encoding="utf-8-sig") as archivo:
            escritor = csv.writer(archivo)
            # ----- Encabezados con unidades -------
            encabezados = [
                "ID", "Fecha y Hora",
                "Tensión (V)", "Resistencia Carga (Ω)", "Material",
                "Longitud Ida (m)", "Sección Transversal (mm²)",
                "Resistencia Cable (Ω)", "Resistencia Total (Ω)",
                "Corriente Estimada (A)", "Caída Tensión Cable (V)",
                "Potencia Disipada (W)"
            ]
            escritor.writerow(encabezados)

            # Recorremos el historial con un ciclo for normal
            for fila in historial:
                entradas = fila.get("entradas", {})
                resultados = fila.get("resultados", {})

                material = entradas.get("material", "")
                material = material.capitalize() if material else "N/A"

                escritor.writerow([
                    fila.get("id", "N/A"),
                    fila.get("fecha", "N/A"),
                    entradas.get("tension", "N/A"),
                    entradas.get("resistencia_carga", "N/A"),
                    material,
                    entradas.get("longitud_ida", "N/A"),
                    entradas.get("seccion_transversal", "N/A"),
                    round(resultados.get("resistencia_cable", 0), 4),
                    round(resultados.get("resistencia_total", 0), 4),
                    round(resultados.get("corriente_estimada", 0), 4),
                    round(resultados.get("caida_tension_cable", 0), 4),
                    round(resultados.get("potencia_disipada", 0), 4)
                ])

        logger.info(f"Reporte CSV exportado exitosamente a: {ruta_csv}")
        return str(ruta_csv)

    except Exception as error:
        logger.error(f"Error al exportar el CSV: {error}")
        return None
