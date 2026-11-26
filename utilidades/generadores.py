# Generador para recorrer el historial
from servicios.historial import leer_historial

# Generador para recorrer el historial con filtros
def generar_historial(filtro_fecha=None, filtro_material=None):
    historial = leer_historial()

    for registro in historial:
        # Validar fecha (si se proporciono un filtro)
        cumple_fecha = True
        if filtro_fecha:
            cumple_fecha = filtro_fecha in registro.get("fecha", "")
        
        # Validar material (si se proporciono un filtro)
        cumple_material = True
        if filtro_material:
            material_registro = registro["entradas"].get("material", "").lower()
            cumple_material = (material_registro == filtro_material.lower())
        
        # Si cumple ambas condiciones, lo producimos con yield
        if cumple_fecha and cumple_material:
            yield registro