import streamlit as st
from Calculadora.matematica import modelo_matematico
from Calculadora.validaciones import validar_entradas
from servicios.historial import guardar_calculo
from servicios.logs import logger
from utilidades.decoradores import medir_tiempo


@medir_tiempo # tiempor que tarda una funcion en recorrerse
#------ Funcion para validar y calcular -------
def procesar_calculo(tension, resistencia_carga, material, longitud_ida, seccion_transversal):   
    v, r, m, l, a = validar_entradas(tension, resistencia_carga, material, longitud_ida, seccion_transversal)
    #validamos las entradas y asignarlo en esas variables para escribir menos
    resultados = modelo_matematico(v, r, m, l, a)  
    # Calculamos las los datos entrantes
    return v, r, m, l, a, resultados
    #retornamos los datos ya validados con los resultados

def pagina_calculadora():   # Toda la sección de calculadora
    st.title(" Calculadora de Circuitos DC")
    st.write("Ingresa los datos del circuito para calcular la corriente, la caída de la tensión y la potencia")
    st.write("---")

    with st.container (border = True):   # contenedor
        st.markdown("###  Datos del Circuito ")

        with st.form("formulario_calculo"):  #formulario
            col1, col2 = st.columns(2)   # 2 columnas simetricas
            with col1:
            #----input de tensión-----
                tension=st.number_input("**Tensión de la fuente (v) —** *Ejemplo: 12*" , step = 1.0, key = "tension_input") 
            with col2:
            # ----Input de resistencia-----
                resistencia_carga=st.number_input("**Resistenacia de la carga (Ω) —** *Ejemplo: 10*", step = 1.0, key = "resistencia_input")

            col3, col4 = st.columns(2)

            with col3:
            #---- menu de input de material ----
            # Se guardan los input en el espacio de memoria especificado para poder controlarlos 
                material=st.selectbox("**Material —** *Ejemplo: Plata* ",["Cobre", "Oro", "Plata", "Aluminio"], key = "material_input")
            with col4: 
            #---- Input de longuitud de ida ----
                longitud_ida=st.number_input("**Longitud de ida (m) —** *Ejemplo: 5*", step = 1.0, key = "longitud_input")
            
            st.write("")
            # --Input de seccion transversal--
            seccion_transversal=st.text_input("**Sección transversal (mm²) —**  *Ejemplo: 2.5mm²*", key = "seccion_input")
            st.write("")

            #---boton que guarda los datos en la variable---
            boton_calcular=st.form_submit_button("Calcular resultados ", type="primary", use_container_width=True)

    boton_limpiar = st.button("Limpiar resultados", type="secondary", use_container_width=True)

    if boton_limpiar:
        # 1. Borramos las claves de la memoria de Streamlit
        # Ciclo for para no repetir 5 veces 
        # se crea la lista con los espacios de memoria a manipular
        claves_a_borrar = ["tension_input", "resistencia_input", "material_input", "longitud_input", "seccion_input"]
        for clave in claves_a_borrar:     # ciclo for para evitar if 
            if clave in st.session_state:   # si el espacio de memoria existe (si tiene memoria)
                del st.session_state[clave]   # Eliminar el espacio de la memoria  
        st.rerun()      
         # recarga la pagina par volve a poner inputs


    if boton_calcular: #cuando se precione el boton
        try:
            #----- Se validan + calculan los datos -----
            v, r, m, l, a, resultados = procesar_calculo(tension, resistencia_carga, material, longitud_ida, seccion_transversal)
        #----- Se sacan los datos retornados de la función -----

        #----- Ya validados se preparan para ser guardados en el json -----
            entradas_dict={   # dicionario con lo datos de entrada 
                "tension": v,
                "resistencia_carga": r,
                "material": m,
                "longitud_ida": l,
                "seccion_transversal": a,
            }
            id_guardado = guardar_calculo(entradas_dict, resultados)
            logger.info(f"Cálculo ID {id_guardado} guardado con éxito.")

            st.success(f" Cálculo realizado con exito.")
            st.write("---")

            #Mostrar resultados
            st.title("Resultados Obtenidos  ")

            #organizar con columnas primera fila
            result_col1, result_col2, result_col3 = st.columns(3)   #3 partes iguales
            result_col1.metric(  #que se vea Grande
                label = "Resistencia del cable (Rc)",  #descripcion
                value = f"{resultados['resistencia_cable']:.4f} Ω"  # valor redondeado a 4 decimales
            )

            result_col2.metric(
                label = "Resistencia total (Rt)",
                value = f"{resultados['resistencia_total']:.4f} Ω"
            )

            result_col3.metric(
                label = "Corriente Estimada (I)",
                value = f"{resultados['corriente_estimada']:.4f} A"
            )

            # fila 2

            result_col4, result_col5 = st.columns(2)
            result_col4.metric(
                label = "Caída de tensión del cable (Vc)",
                value = f"{resultados['caida_tension_cable']:.4f} V"
            
            )

            result_col5.metric(
                label = "Potencia disipada en cable (Pc)",
                value = f"{resultados['potencia_disipada']:.4f} W"
            )

            #Muestra adicional

            with st.expander("Muestra de conversión y longitud"):   # recuadro que se expande
                st.write(f"**Área converitida a m²:** {resultados['conversion_area']} m²")   
                st.write(f"**Logitud total del cable ida y vuelta:** {resultados['longitud_total']} m")

            #--------Repaso de los datos ingresados-------
            st.warning(f"""
                    Datos utilizados para realizar este calculo:
                    * Tensión: {v} V
                    * Resistencia de carga: {r} Ω 
                    * Material: {(m.title())} 
                    * Longitud: {l} m
                    * Sección transversal: {a} mm²
                    """)


        except ValueError as error:  # gualda ValueError en la variable para que no reaccione
            st.error(f" Error de validación: {error}")  # mensajito de error
            st.info("Asegurate de ingresar datos mayores a cero (0) y que el formato de la sección transversal ingresada sea correcta")
            # Mesaje de sugerencia 



