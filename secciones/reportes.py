import streamlit as st
import os
from servicios.historial import leer_historial
from servicios.reportes import exportar_csv


def pagina_reportes():
    st.title(" Reportes")
    st.write("Descarga el historial de tus cálculos en formato CSV para poderlos usar en excel u otras herramientas.")
    st.write("---")

    historial = leer_historial()    # Leer el historial actual

    if not historial:  # Si está vacío
        st.warning("**No hay cálculos en el historial para poder exportarlos**")
        st.info("**Aún no hay cálculos en el historial,** ve a la sección de *Calculadora* o presiona **¡CALCULAR YA!** para ser redirigido y realiza tu primer cálculo ")
        st.write("---")

        #---Boton de Cacular ya ----
        from secciones.menu_tabs import CALCULADORA
        if st.button("**¡CALCULAR YA!** ", type="primary", use_container_width=True ):  #boton ancho
            st.switch_page(CALCULADORA)   #redireccion
        return

    # Resumen rapido
    st.markdown("### Resumen de datos")
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Total de cálculos guardados", len(historial))
    # --- Ultimo ID pa tener una idea 
    with col2:
        ultimo_id = historial[-1].get ("id", "N/A")
        st.metric("Último registro generado (último ID)", ultimo_id )

    st.write("---")    

    with st.container(border=True):
        st.markdown("### Datos a exportar")
        st.write("Así se veran tus datos en el archivo")

        # Guardar los calculos a exportar de la tabla (misma lógica que en Historial)
        datos_tabla = []
        for c in historial:
            datos_tabla.append({
                "ID": c["id"],
                "Fecha": c["fecha"],
                "Material": c["entradas"]["material"].capitalize(),
                "Tensión (V)": c["entradas"]["tension"],
                "R. Carga (Ω)": c["entradas"]["resistencia_carga"],
                "Longitud (m)": c["entradas"]["longitud_ida"],
                "Sección (mm²)": c["entradas"]["seccion_transversal"],
                "Rc (Ω)": round(c["resultados"]["resistencia_cable"], 4),
                "Rt (Ω)": round(c["resultados"]["resistencia_total"], 4),
                "I (A)": round(c["resultados"]["corriente_estimada"], 4),
                "Vc (V)": round(c["resultados"]["caida_tension_cable"], 4),
                "Pc (W)": round(c["resultados"]["potencia_disipada"], 4),
            })
        st.dataframe(datos_tabla, use_container_width=True, hide_index=True)
        st.write("---")


        if st.button("**Generar archivo CSV**", type="primary", use_container_width=True):
            with st.spinner("Procesando datos y generando archivo"):
                ruta_archivo = exportar_csv(historial)

                if ruta_archivo and os.path.exists(ruta_archivo):
                    with open (ruta_archivo, "r", encoding="utf-8-sig" ) as f:
                        datos_csv = f.read()

                    st.download_button(
                        label= "Guardar archivo en computadora",
                        data = datos_csv,
                        file_name = "reporte_calculos_electricos.csv",
                        mime = "text/csv",
                        use_container_width=True

                    )
                    st.success("Archivo generado con exito, has click en el boton de arriba para guardarlo")
                else:
                    st.error("Upps.. Surgio un problema al generar el archivo, recomendamos revisar el log para consultar con los detalles técnicos")
