import streamlit as st

def pagina_fundamentos():
    st.title(" Fundamentos y Ayuda")
    st.write("Bienvenido a la sección de documentación del simulador. Aquí encontrarás toda la teoría y las reglas que utiliza la aplicación para realizar los cálculos.")
    st.write("---")

    # Creamos 4 pestañas para organizar la información
    tab1, tab2, tab3, tab4 = st.tabs([
        " Parámetros de Entrada", 
        " Fórmulas Matemáticas", 
        " Caso de Comprobación", 
        " Supuestos y Limitaciones"
    ])

    # --- PESTAÑA 1: PARÁMETROS ---
    with tab1:
        st.header("Datos solicitados al usuario")
        st.write("Para realizar el calculo, el sistema solicita los siguientes 5 parámetros:")
        
        st.markdown("""
        *   **Tensión (V):** Voltaje DC suministrado por la fuente, en voltios (Ej: 12 V). Debe ser mayor que cero.
        *   **Resistencia de Carga (Rcarga):** Resistencia del dispositivo conectado, en ohmios (Ej: 10 Ω). Debe ser mayor que cero.
        *   **Material (ρ):** Selector fijo (cobre, aluminio, oro, plata). Determina la resistividad usada.
        *   **Longitud de ida (L):** Distancia fuente-carga en metros (Ej: 5 m). El sistema duplica este valor para representar el retorno.
        *   **Sección transversal (A):** Área del material conductor en mm² (Ej: 2,5 mm²). Debe ser mayor que cero.
        """)

    # --- PESTAÑA 2: FÓRMULAS ---
    with tab2:
        st.header("Modelo Matemático")
        st.write("El circuito se modela de forma ideal en serie (fuente + conductor de ida + carga + conductor de retorno). Los cálculos se realizan en estricto orden:")
        
        st.write("**1. Conversión de área a metros cuadrados:**")
        st.latex(r"A (m^2) = A (mm^2) \times 10^{-6}")

        st.write("**2. Longitud total del conductor (ida y retorno):**")
        st.latex(r"L_{total} = 2 \times L")

        st.write("**3. Resistencia del cable (Rc):**")
        st.latex(r"R_c = \rho \times \frac{L_{total}}{A (m^2)}")

        st.write("**4. Resistencia total (Rt):**")
        st.latex(r"R_t = R_{carga} + R_c")

        st.write("**5. Corriente estimada (I) aplicando la Ley de Ohm:**")
        st.latex(r"I = \frac{V}{R_t}")

        st.write("**6. Caída de tensión en el cable (Vc):**")
        st.latex(r"V_c = I \times R_c")

        st.write("**7. Potencia disipada en el cable (Pc):**")
        st.latex(r"P_c = I^2 \times R_c")

    # --- PESTAÑA 3: EJEMPLO ---
    with tab3:
        st.header("Caso de Comprobación")
        st.write("Para verificar el correcto funcionamiento del sistema, se utiliza el siguiente caso de referencia:")
        
        st.info("""
        **Entradas:**
        *   **V:** 12 V
        *   **Rcarga:** 10 Ω
        *   **Material:** Cobre (ρ = 1,68 × 10⁻⁸ Ω·m)
        *   **L:** 5 m (Ida)
        *   **A:** 2,5 mm²
        """)

        st.success("""
        **Resultados esperados (sin redondeos intermedios):**
        *   **Rc (Resistencia del cable):** 0,0672 Ω
        *   **Rt (Resistencia total):** 10,0672 Ω
        *   **I (Corriente):** 1,1920 A
        *   **Vc (Caída de tensión):** 0,0801 V
        *   **Pc (Potencia disipada):** 0,0955 W
        """)
        
        st.write("Si ingresas estos mismos datos en la pestaña de **Calculadora**, los resultados deben coincidir exactamente con los mostrados aquí.")

    # --- PESTAÑA 4: LIMITACIONES ---
    with tab4:
        st.header("Alcance y Seguridad")
        st.warning(" **Aviso importante:** Esta es una simulación didáctica de un circuito DC ideal a 20 °C.")
        
        st.write("La aplicación tiene las siguientes limitaciones estrictas:")
        st.markdown("""
        *   **No calcula ampacidad** ni la corriente máxima admisible del cable.
        *   **No sirve para dimensionar** instalaciones eléctricas reales.
        *   **No considera calentamiento**, resistencia de contactos ni otros efectos no incluidos en las fórmulas.
        *   **No considera caídas de tensión** por otros componentes fuera del cable de ida y retorno.
        """)
        st.write("El propósito de esta herramienta es meramente académico para la cátedra de **Programación I**.")