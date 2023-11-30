import streamlit as st
from utils import *

# Establecer la configuración de la página para un tema y un título
st.set_page_config(page_icon="👨‍⚕️", page_title="Detección de Neumonía", layout="centered")

st.header("Proyecto :ambulance:", anchor="large")

# Título y subida de imagen
st.image("https://content21.sabervivirtv.com/medio/2021/01/11/neumonia-ficha_f1171fba_1280x720.jpg", width=750)
st.title("Detección de Neumonía por Virus o Bacterias :mask:")

st.markdown("### Resumen del Proyecto")
st.markdown("""
    **Objetivo del Proyecto:** Desarrollar un sistema de IA para diagnosticar neumonía y determinar su origen (viral o bacteriano) a partir de radiografías pulmonares.
    
    **Equipo del Proyecto:**
    - Sebastián Rendón Patiño
    - Andrés Felipe Aristizábal Miranda
""")

c30, c31 = st.columns([9, 1])  
    
with c30:
    st.markdown("""
    ## Sube tu imagen de Rayos X en formato .jpeg
""")
    archivo_subido = st.file_uploader("", type="jpeg", key="1")
    if archivo_subido is not None:
        with st.spinner('Analizando imagen...'):
            # Lógica para leer datos y predecir
            dato = leer_datos(archivo_subido)
            modelo = cargar_modelo() 
            prediccion = predecir(modelo=modelo, dato=dato)
            categoria = obtener_categoria(prediccion=prediccion)
            
            # Visualización de resultados
            if categoria == 'Normal':
                st.success("La imagen de Rayos X corresponde a una persona que está sana.")
            elif categoria == 'Bacteria':
                st.success("La imagen de Rayos X corresponde a una persona que tiene neumonía producto de una bacteria.")
            elif categoria == 'Virus':
                st.success("La imagen de Rayos X corresponde a una persona que tiene neumonía producto de un virus.")