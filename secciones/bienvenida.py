import streamlit as st    
import os     # libreria para verificar si existe la imagen

def pagina_bienvenida():
   
    st.markdown(
         "<h1 style='text-align: center;'>Cátedra: programación I</h3>", unsafe_allow_html=True,
        )   # Titulo centrado

    col1, col2, = st.columns([1, 1.2])    # Dividir espacios en 2 mitades iguales
    with col1:             # Primera mitad izquierda
        if os.path.exists("calculadora.png"):   # Si existe la imagen
            st.image("calculadora.png", width=550)  
        else:
            st.info("La imagen no se encuentra en la carpeta del proyecto. Por favor, asegúrese de que el archivo 'calculadora.png' esté presente.")   # sino mensajito de alerta



    with col2:
        st.markdown("<br><br><br>", unsafe_allow_html= True)
        st.markdown("### Bienvenido a la Calculadora")
        st.write("""
        Esta aplicación web permite calcular la corriente eléctrica, y la caida de la tensión 
        y la potencia disipada en un circuito sencillo de corriente continua (DC).
                
        👈 **Utiliza el menú lateral para navegar.**
               
        **Calculadora:** Ingresa los valores y obtén los resultados de corriente, caída de tensión y potencia disipada.
        
        **Historial:** Consulta y exporta tus cálculos anteriores.
        
        **Logs:** Visualiza los eventos técnicos del sistema.
         """)
