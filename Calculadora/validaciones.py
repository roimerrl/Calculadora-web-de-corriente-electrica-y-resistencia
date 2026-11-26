import math
import re
from Calculadora.materiales import materiales
from servicios.logs import logger


def validar_numero_positivo(valor, nombre_campo):
    """
    Función auxiliar para validar tensión, resistencia y longitud.
    Verifica que no esté vacío, que sea un número, que sea finito y mayor a cero.
    """
    if valor is None or str(valor).strip() == "":
        logger.warning(f"Validacion rechazada: {nombre_campo} vacio.")
        raise ValueError(f"El campo '{nombre_campo}' no puede estar vacio.")

    try:
        # Convertimos a texto, quitamos espacios y cambiamos coma por punto
        texto_limpio = str(valor).strip().replace(",", ".")
        numero = float(texto_limpio)
    except ValueError:
        logger.warning(f"Validacion rechazada: {nombre_campo} no es numerico ({valor}).")
        raise ValueError(f"El campo '{nombre_campo}' debe ser un numero valido.")

    # math.isfinite() descarta valores infinitos (inf) y NaN (Not a Number)
    if not math.isfinite(numero) or numero <= 0:
        logger.warning(f"Validacion rechazada: {nombre_campo} fuera de rango ({valor}).")
        raise ValueError(f"El campo '{nombre_campo}' debe ser un numero finito mayor a cero.")

    return numero


def validar_entradas(tension, resistencia_carga, material, longitud_ida, seccion_transversal):
    r"""
    Valida los 5 parámetros de entrada del circuito DC.

    - Patrón utilizado: ^\d+([.,]\d+)?\s*(mm2|mm²)?$ (ignora mayúsculas y minúsculas)
      * ^ y $ : Obliga a que todo el texto cumpla el formato de principio a fin.
      * \d+ : Exige uno o más dígitos enteros al inicio.
      * ([.,]\d+)? : Permite de forma opcional un punto o coma seguido de decimales.
      * \s* : Permite cero o más espacios antes de la unidad.
      * (mm2|mm²)?: Permite de forma opcional la unidad mm2 o mm².
    - Formatos admitidos: "2.5", "2,5", "2.5 mm2", "2,5 mm²", "4"
    - Formatos rechazados: "" (vacío), "-2.5" (negativos), "0" (cero), "abc" (texto),
      "2." (decimal incompleto), "2.5 cm" (unidades no permitidas).
    """
    # 1, 2 y 3. Validar Tensión, Resistencia de carga y Longitud de ida
    tension = validar_numero_positivo(tension, "Tensión")
    resistencia_carga = validar_numero_positivo(resistencia_carga, "Resistencia de carga")
    longitud_ida = validar_numero_positivo(longitud_ida, "Longitud de ida")

    # 4. Validar Material
    if material is None or str(material).strip() == "":
        logger.warning("Validacion rechazada: Material no seleccionado.")
        raise ValueError("Debe seleccionar un material conductor.")

    material_limpio = str(material).strip().lower()
    dic_materiales = materiales()

    if material_limpio not in dic_materiales:
        logger.warning(f"Validacion rechazada: Material no permitido ({material}).")
        opciones = ", ".join(dic_materiales.keys())
        raise ValueError(f"Material no válido. Opciones disponibles: {opciones}.")

    # 5. Validar Sección Transversal con Regex
    if seccion_transversal is None or str(seccion_transversal).strip() == "":
        logger.warning("Validacion rechazada: Seccion transversal vacia.")
        raise ValueError("La sección transversal no puede estar vacía.")

    seccion_texto = str(seccion_transversal).strip()

    # Se rechaza negativos con un mensaje específico
    if seccion_texto.startswith("-"):
        logger.warning(f"Validacion rechazada: Seccion negativa ({seccion_texto}).")
        raise ValueError("La sección transversal no puede ser negativa.")

    patron = r"^\d+([.,]\d+)?\s*(mm2|mm²)?$"
    if not re.match(patron, seccion_texto, re.IGNORECASE):
        logger.warning(f"Validacion rechazada: Formato de seccion invalido ({seccion_texto}).")
        raise ValueError("Formato de sección inválido. Use ejemplos como: 2.5, 2,5, 2.5 mm2 o 2,5 mm².")

    # Se convierte en minuscula por si acaso y se limpia y cambiamos coma por punto para convertir a float
    numero_texto = (
        seccion_texto.lower()
        .replace("mm2", "")
        .replace("mm²", "")
        .replace(",", ".")
        .strip()
    )
    seccion_float = float(numero_texto)

    if seccion_float <= 0:
        logger.warning(f"Validacion rechazada: Seccion igual a cero ({seccion_texto}).")
        raise ValueError("La sección transversal debe ser mayor a cero.")

    logger.info("Validaciones de entrada superadas correctamente.")
    return tension, resistencia_carga, material_limpio, longitud_ida, seccion_float