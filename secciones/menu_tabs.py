import streamlit as st
import os
from secciones.fundamentos_ayuda import pagina_fundamentos
from secciones.bienvenida import pagina_bienvenida
from secciones.calculadora import pagina_calculadora
from secciones.historial import pagina_historial
from secciones.logs import pagina_logs
from secciones.reportes import pagina_reportes
from secciones.conocenos import pagina_conocenos


def navegacion():
    # 1. Ponemos el logo centrado usando 3 columnas
    col_izq, col_logo, col_der = st.sidebar.columns([1, 2, 1])
    with col_logo:
        st.image("logo-2.png", use_container_width=True)
        
    
    st.sidebar.markdown(
        "<p style='text-align: center; font-size: 12px; color: gray;'>Proyecto Final - Programación I</p>", 
        unsafe_allow_html=True
    )
    st.sidebar.write("---") # Línea separadora

    #------Menu de navegación------
    nav = st.navigation(
        {
            "Principal":[
                st.Page(pagina_bienvenida, title="Bievenida", icon="🏠"),
                st.Page(pagina_calculadora, title="Calculadora", icon="🧮"),
                st.Page(pagina_historial, title="Historial", icon="📚"),
                st.Page(pagina_reportes, title="Reportes", icon="📊"),
            ],

            "Sistema": [
                st.Page(pagina_logs, title="Logs Técnicos", icon="🗒️"),
            ],

            "Información":[
                st.Page(pagina_fundamentos, title="Fundamentos / Ayuda", icon="📖"),
                st.Page(pagina_conocenos, title="Conocenos", icon="👥"),
            ]
        },
        position="sidebar", #posicion en el menu lateral
    )
    
    nav.run()