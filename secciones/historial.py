import streamlit as st
from servicios.historial import leer_historial
from servicios.logs import logger
from utilidades.generadores import generar_historial

def pagina_historial():
    st.title(" Historial de Cálculos")
    st.write("Consulta todos los cálculos anteriormente realizados.")
    st.write("---")

    historial = leer_historial()

    if len(historial) == 0:
        st.warning("**Aún no hay calculos en el historial,** ve a la sección de *Calculadora* o presiona **¡CALCULAR YA!** para ser redirigido y realiza tu primer cálculo ")
        st.write("---")

        #---Boton de Cacular ya ----
        from secciones.menu_tabs import CALCULADORA
        if st.button("**¡CALCULAR YA!** ", type="primary", use_container_width=True ):  #boton ancho
            st.switch_page(CALCULADORA)   #redireccion
        return # lanza none 

    # Si hay algo en el json aparecera lo siguiente 
    with st.container(border=True):
        st.markdown("### Filtros para tus busquedas")

        col1, col2, = st.columns(2)

        #---- Filtro de material----
        with col1:
            # Se toman del diccionario de materiales: si mañana agregan otro, el filtro lo incluye
            from Calculadora.materiales import materiales
            opciones_materiales = ["Todos"] + [m.capitalize() for m in materiales()]
            filtro_material = st.selectbox("**Seleccione el material a filtrar**", opciones_materiales, key="filtro_material")

        #----Filtro de fecha----
        with col2:
            filtro_fecha = st.text_input("**Ingrese fecha a filtrar** — *Ej: 2026-11-25:*", "", key="filtro_fecha")

        
        st.write("")
        limpiar_filtro = st.button("Limpiar filtro",type="primary" , use_container_width=True)

    if limpiar_filtro:
        # Se borran las claves de los widgets de la memoria de Streamlit;
        # solo reasignar las variables locales NO limpiaba los controles.
        for clave in ("filtro_material", "filtro_fecha"):
            if clave in st.session_state:
                del st.session_state[clave]
        st.rerun()

        
        # convertimos el  input en minuscula para comparar con el json
    if filtro_material == "Todos":
        filtro_material_lower = None
    else:
        filtro_material_lower = filtro_material.lower()

    if filtro_fecha != "":       # si tiene algo se guarda en el validado sino se deja vacio
        filtro_fecha_valido = filtro_fecha
    else:
        filtro_fecha_valido = None

    # produce un registro a la ves 
    historial_filtrado = list(generar_historial(filtro_fecha_valido, filtro_material_lower))


    if len(historial_filtrado) == 0:  # si json esta vacio en ese filtro 
        # Registramos el aviso en los logs (WARNING: no detiene la aplicación)
        logger.warning("Filtro del historial sin coincidencias.")
        st.warning("**No se encontraron calculos en esta filtración**")
        return
    st.write("")
    st.success(f"**Registros encontrados con exito:** {len(historial_filtrado)}")
    st.write("---")

    # Pre-organizamos la muestra de datos para agregarlo en una lista y mostrarlo como tabla
    datos_tabla = []

    for c in historial_filtrado:   #transpapelamos los datos filtrados
        datos_tabla.append({        
            "ID": c["id"],
            "Fecha": c["fecha"],
            "Material": c["entradas"] ["material"].capitalize(),
            "Tensión (V)": c["entradas"]["tension"],
            "Resistencia (Ω)": c["entradas"] ["resistencia_carga"],
            "Longitud (m)": c["entradas"]["longitud_ida"],
            "Sección (mm²)": c["entradas"] ["seccion_transversal"],
            "Resistencia del cable - Rc (Ω)": round(c["resultados"] ["resistencia_cable"], 4),
            "Resistencia total - Rt (Ω)": round(c["resultados"]["resistencia_total"], 4),
            "Corriente - I (A)": round(c["resultados"]["corriente_estimada"], 4),
            "Caida de la tensión del cable - Vc (V)": round(c["resultados"]["caida_tension_cable"], 4),
            "Potencia disipada - Pc (W)": round(c["resultados"]["potencia_disipada"], 4),


        })

    # mostramos la tabla 
    st.markdown("### Tabla de Calculos")
    st.table(datos_tabla)
    st.write("---")

# tarjeta individual por id 
    st.markdown("###  Detalles de cada cálculo")

    for c in historial_filtrado:     #por cada calculo
        with st.expander(f" Calculo ID {c['id']} - {c['fecha']}"):  #Crear tarjeta
            col_det1, col_det2 = st.columns(2)            # columnas dentro de la tarjeta

            with col_det1:
                st.markdown("##### **Datos de entrada:**")
                st.write(f"* **Tensión:** {c['entradas']['tension']} V")
                st.write(f"* **Resistencia de carga:** {c['entradas']['resistencia_carga']} Ω")
                st.write(f"* **Material:** {c['entradas']['material'].capitalize()}")
                st.write(f"* **Longitud de ida:** {c['entradas']['longitud_ida']} m")
                st.write(f"* **Sección transversal:** {c['entradas']['seccion_transversal']} mm²")

            with col_det2:
                st.markdown("##### **Resultados:**")
                st.write(f"* **Rc:** {c['resultados']['resistencia_cable']:.4f} Ω")
                st.write(f"* **Rt:** {c['resultados']['resistencia_total']:.4f} Ω")
                st.write(f"* **I:** {c['resultados']['corriente_estimada']:.4f} A")
                st.write(f"* **Vc:** {c['resultados']['caida_tension_cable']:.4f} V")
                st.write(f"* **Pc:** {c['resultados']['potencia_disipada']:.4f} W")






        