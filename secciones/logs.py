import streamlit as st

from servicios.logs import generar_eventos, RUTA_LOG

# Cantidad de eventos recientes que se muestran en la tabla
EVENTOS_RECIENTES = 50


def pagina_logs():
    st.title(" Logs Técnicos del sistema")
    st.write("Consulta los eventos tecnicos registrados por la aplicación (inicio, cálculos, validaciones y errores).")
    st.write("---")

    # Validar si el archivo existe
    if not RUTA_LOG.exists():
        st.warning("Aún no se han realizado registros, has un calculo para verlos aquí. ")
        from secciones.menu_tabs import CALCULADORA
        if st.button("**¡CALCULAR YA!** ", type="primary", use_container_width=True):  # boton ancho
            st.switch_page(CALCULADORA)   # redireccion
        return

    # Consumimos el generador: produce los eventos uno a uno (yield)
    eventos = list(generar_eventos())

    if not eventos:
        st.info("El archivo de logs existe pero no contiene información.")
        return

    # Tomamos los últimos 50 para no saturar la pantalla,
    # ordenados de más reciente a más antiguo
    eventos_recientes = eventos[-EVENTOS_RECIENTES:]
    eventos_recientes.reverse()

    # Contadores por nivel (ciclo for, requisito del enunciado)
    info_contador = 0
    warning_contador = 0
    error_contador = 0
    for evento in eventos_recientes:
        if evento["nivel"] == "INFO":
            info_contador += 1
        elif evento["nivel"] == "WARNING":
            warning_contador += 1
        elif evento["nivel"] == "ERROR":
            error_contador += 1

    st.markdown("### Eventos recientes")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.metric("Eventos de INFO", info_contador)
    with col2:
        st.metric("Eventos de WARNING", warning_contador)
    with col3:
        st.metric("Eventos de ERROR", error_contador)

    st.write("---")

    # Tabla con los últimos 50 eventos
    with st.container(border=True):
        st.markdown(f"### Registro de los ultimos {EVENTOS_RECIENTES} detalles")

        datos_logs = []
        for evento in eventos_recientes:
            datos_logs.append({
                "Fecha/Hora": evento["fecha"],
                "Nivel": evento["nivel"],
                "Módulo": evento["modulo"],
                "Mensaje": evento["mensaje"],
            })

        st.dataframe(datos_logs, use_container_width=True, hide_index=True)

    st.write("---")
    st.caption("Los logs se guardan en **logs/app.log** y no se borran al reiniciar la aplicación.")
