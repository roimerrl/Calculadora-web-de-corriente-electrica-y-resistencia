import streamlit as st
from utilidades.rutas import RUTA_LOGO
from servicios.logs import logger
from secciones.bienvenida import pagina_bienvenida
from secciones.calculadora import pagina_calculadora
from secciones.historial import pagina_historial
from secciones.logs import pagina_logs
from secciones.reportes import pagina_reportes
from secciones.fundamentos_ayuda import pagina_fundamentos
from secciones.conocenos import pagina_conocenos


    #definimos las paginas como variables para que funcionen con botones
BIENVENIDA=st.Page(pagina_bienvenida, title="Bienvenida", icon="🏠")
CALCULADORA=st.Page(pagina_calculadora, title="Calculadora", icon="🧮")
HISTORIAL=st.Page(pagina_historial, title="Historial", icon="📚")
REPORTES=st.Page(pagina_reportes, title="Reportes", icon="📊")
LOGS=st.Page(pagina_logs, title="Logs Técnicos", icon="🗒️")
FUNDAMENTOS_AYUDA=st.Page(pagina_fundamentos, title="Fundamentos / Ayuda", icon="📖")
CONOCENOS=st.Page(pagina_conocenos, title="Conocenos", icon="👥")

def navegacion():
    # Registramos el inicio de la aplicación en los logs.
    # Streamlit vuelve a ejecutar este archivo con cada interacción, así que
    # usamos la memoria de sesión para registrar "inicio" solo una vez.
    if "sesion_iniciada" not in st.session_state:
        st.session_state.sesion_iniciada = True
        logger.info("Aplicación iniciada por el usuario.")

    # 1. Ponemos el logo centrado usando 3 columnas
    col_izq, col_logo, col_der = st.sidebar.columns([1, 2, 1])
    with col_logo:
        # Usamos la ruta calculada desde la raíz del proyecto para que
        # el logo cargue sin importar desde qué carpeta se ejecute la app
        if RUTA_LOGO.exists():
            st.image(str(RUTA_LOGO), use_container_width=True)


    st.sidebar.markdown(
        "<p style='text-align: center; font-size: 12px; color: gray;'>Proyecto Final - Programación I</p>",
        unsafe_allow_html=True
    )
    st.sidebar.write("---") # Línea separadora

    #------ Menu de navegación------
    nav = st.navigation(
        {
            "Principal":[
                BIENVENIDA,
                CALCULADORA,
                HISTORIAL,
                REPORTES,
            ],

            "Sistema": [
                LOGS,
            ],

            "Información":[
                FUNDAMENTOS_AYUDA,
                CONOCENOS,
            ]
        },
        position="sidebar", #posicion en el menu lateral
    )

    nav.run()
