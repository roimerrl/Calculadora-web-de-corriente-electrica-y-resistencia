import streamlit as st    
import os     # libreria para verificar si existe la imagen

def pagina_bienvenida():
    st.title(" Bienvenido a la Calculadora de Circuitos DC")
    st.success("Esta aplicación web permite calcular la corriente eléctrica, y la caida de la tensión y la potencia disipada en un circuito sencillo de corriente continua (DC).")
    st.write("---")

    col1, col2, = st.columns([1, 1.5])    # Dividir espacios en 2 mitades iguales

    # ------------ Columna Izquierda ----------
    with col1:             # Primera mitad izquierda
        if os.path.exists("calculadora.png"):   # Si existe la imagen
            st.image("calculadora.png", width=385)  
        else:
            st.error("La imagen no se encuentra en la carpeta del proyecto. Por favor, asegúrese de que el archivo 'calculadora.png' esté presente.")   # sino mensajito de alerta


    # ----------- columna derecha ----------
    with col2:
        
        st.markdown(
                 "<h1 style='text-align: center;'>Cátedra: programación I</h3>", unsafe_allow_html=True,
                )   # Titulo centrado
        st.write("") # espacio en blanco
        #------ Descripción directa------
        st.write("""
        
                
        *  **Calculadora:** Ingresa los valores y obtén los resultados del cálculo.
        *  **Historial:** Consulta y exporta tus cálculos anteriores.
        *  **Reportes:** Descarga tus resultados en formato CSV.
        *  **Logs:** Visualiza los eventos técnicos del sistema.
        *  **Ayuda:** Aprende sobre las fórmulas y limitaciones.
        *  **Conocenos:** Conoce al equipo desarrollador.
         """)
        st.write("")  # espacio en blanco

        # importamos la variable de la pagina
        from secciones.menu_tabs import CALCULADORA
        if st.button("**¡CALCULAR YA!** ", type="primary", use_container_width=True ):  #boton ancho
            st.switch_page(CALCULADORA)   #redireccion