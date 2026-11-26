import streamlit as st
from secciones.menu_tabs import navegacion


st.set_page_config(     #configuracion inicial de la app
    page_title="Calculadora DC",         #Titulo
    page_icon="🧮",                   
    layout="wide", # Hace que la app use todo el ancho de la pantalla
    initial_sidebar_state="expanded", # El menu lateral se muestra automáticamente
)

navegacion()
