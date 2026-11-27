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

    # -----------------------------------------------------------------
    # Estilos de color de la aplicación (Aqui me rendi y pedí ayuda))
    # -----------------------------------------------------------------
    st.markdown(
        """
        <style>
        /* 1. Barra de color arriba de la pagina */
        .barra-color {
            height: 8px;
            border-radius: 10px;
            background: linear-gradient(90deg, #00c6ff, #0072ff, #8f00ff, #00e676);
            margin-bottom: 1rem;
        }
        /* 2. Titulos con color */
        [data-testid="stHeadingWithActionElements"] h1,
        [data-testid="stMarkdownContainer"] h1,
        h1 { color: #0a4bd6 !important; }
        [data-testid="stMarkdownContainer"] h2,
        [data-testid="stMarkdownContainer"] h3,
        h2, h3 { color: #17408b !important; }
        /* 3. Menu lateral con degradado suave */
        section[data-testid="stSidebar"] {
            background: linear-gradient(180deg, #e8f2ff 0%, #ffffff 100%);
            border-right: 2px solid #b9d6ff;
        }
        /* 4. Tarjetas de resultados (metricas) con color */
        div[data-testid="stMetric"] {
            background: linear-gradient(180deg, #f0f7ff, #ffffff);
            border-left: 5px solid #00a8ff;
            border-radius: 10px;
            padding: 12px 14px;
            box-shadow: 0 2px 8px rgba(20, 80, 160, 0.12);
        }
        /* 5. Botones con esquinas redondeadas */
        .stButton > button,
        div[data-testid="stFormSubmitButton"] > button {
            border-radius: 10px;
        }
        /* 6. Logo de la universidad mas grande en el menu */
        img[data-testid="stSidebarLogo"] {
            height: 55px !important;
            width: auto !important;
        }
        </style>
        <div class="barra-color"></div>
        """,
        unsafe_allow_html=True,
    )

        # Usamos la ruta calculada desde la raíz del proyecto para que
        # el logo cargue sin importar desde qué carpeta se ejecute la app
    if RUTA_LOGO.exists():
        st.logo(str(RUTA_LOGO), size="large")

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
