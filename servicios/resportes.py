import csv
import os

def exportar_csv(historial):
    if not os.path.exists("reportes"):
        os.mkdir("reportes")

    ruta_csv = "reportes/reporte_calculos.csv"

    if len(historial) == 0:
        return ruta_csv

    archivo = open(ruta_csv, "w", newline="", encoding="utf-8")
    escritor = csv.writer(archivo)
    
    # Escribimos los titulos
    escritor.writerow(["ID", "Fecha", "Tension (V)", "R Carga", "Material", "Longitud", "Seccion", "R Cable", "R Total", "Corriente", "Caida Tension", "Potencia"])

    # Recorremos el historial con un for normal
    for fila in historial:
        entradas = fila["entradas"]
        resultados = fila["resultados"]
        
        escritor.writerow([
            fila["id"], fila["fecha"], 
            entradas["tension"], entradas["resistencia_carga"], entradas["material"], 
            entradas["longitud_ida"], entradas["seccion_transversal"],
            resultados["resistencia_cable"], resultados["resistencia_total"], 
            resultados["corriente_estimada"], resultados["caida_tension_cable"], 
            resultados["potencia_disipada"]
        ])
        
    archivo.close()
    return ruta_csv