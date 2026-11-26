import streamlit as st
from utilidades.rutas import CARPETA_IMAGENES

def pagina_conocenos():
    st.title(" Conócenos")
    st.write("Conoce al equipo de desarrolladores de esta fantástica calculadora web de corriente eléctrica.")  #xD
    st.write("---")


    col1, col2, col3, col4, col5= st.columns([1, 1, 1.5, 1, 1])

    with col2:
        #-----------Esteban Cen----------------
        st.markdown("<h3 style='text-align: center;'>Esteban Cen</h3>", unsafe_allow_html=True)
        if (CARPETA_IMAGENES / "Esteban.png").exists():
            st.image(str(CARPETA_IMAGENES / "Esteban.png"), width=200)
        else:
            st.info("Esteban no quizo aparecer en la foto 😉")
        st.markdown("<p style='text-align: center;'><b>Integrante 1</b></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><i>No dormir se me esta dando bien</i></p>", unsafe_allow_html=True)
        st.write("")

        #-----------Adrian Torres--------------
        st.markdown("<h3 style='text-align: center;'>Adrian Torres</h3>", unsafe_allow_html=True)
        if (CARPETA_IMAGENES / "Adrian.png").exists():
            st.image(str(CARPETA_IMAGENES / "Adrian.png"), width=200)
        else:
            st.info("Adrian no quizo aparecer en la foto 😉")
        st.markdown("<p style='text-align: center;'><b>Integrante 3</b></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><i>Experto en sobrevivir a los fines de semana</i></p>", unsafe_allow_html=True)
        st.write("")

        #-----------José Castillo --------------
        st.markdown("<h3 style='text-align: center;'>José Castillo</h3>", unsafe_allow_html=True)
        if (CARPETA_IMAGENES / "JoseCastillo.png").exists():
            st.image(str(CARPETA_IMAGENES / "JoseCastillo.png"), width=200)
        else:
            st.info("José Castillo no quiso aparecer en la foto 😉")
        st.markdown("<p style='text-align: center;'><b>Integrante 5</b></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><i>Viendo todo en modo oscuro</i></p>", unsafe_allow_html=True)
        st.write("")

    with col4:
        #-----------Roimer Rodríguez--------------
        st.markdown("<h3 style='text-align: center;'>Roimer Rodríguez</h3>", unsafe_allow_html=True)
        if (CARPETA_IMAGENES / "Roimer.png").exists():
            st.image(str(CARPETA_IMAGENES / "Roimer.png"), width=200)
        else:
            st.info("Roimer no quizo aparecer en la foto 😉")
        st.markdown("<p style='text-align: center;'><b>Integrante 2</b></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><i>Empezando a amar el cafe</i></p>", unsafe_allow_html=True)
        st.write("")

        #-----------José Hernández--------------
        st.markdown("<h3 style='text-align: center;'>José Hernández</h3>", unsafe_allow_html=True)
        if (CARPETA_IMAGENES / "JoseHernandez.png").exists():
            st.image(str(CARPETA_IMAGENES / "JoseHernandez.png"), width=200)
        else:
            st.info("José Negro no quizo aparecer en la foto 😉")
        st.markdown("<p style='text-align: center;'><b>Integrante 4</b></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><i>¿Qué es el dia?</i></p>", unsafe_allow_html=True)
        st.write("")

        #-----------Jessena Ibrahim--------------
        st.markdown("<h3 style='text-align: center;'>Jessena Ibrahim</h3>", unsafe_allow_html=True)
        if (CARPETA_IMAGENES / "Jessena.png").exists():
            st.image(str(CARPETA_IMAGENES / "Jessena.png"), width=200)
        else:
            st.info("Jessena no quizo aparecer en la foto 😉")
        st.markdown("<p style='text-align: center;'><b>Integrante 6</b></p>", unsafe_allow_html=True)
        st.markdown("<p style='text-align: center;'><i>Sobreviviendo sin luz</i></p>", unsafe_allow_html=True)