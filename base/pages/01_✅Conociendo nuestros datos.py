import pandas as pd
import streamlit as st

area =  pd.read_csv('area_protegida.csv')
st.title("Parte 1")
st.header("Datos basicos de las areas protegidas de argentina")
filas, columnas = area.shape
with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = area.shape
    st.write(f'Tiene { filas} filas y {columnas} columnas')

# Esto muestra los tipos de datos
with st.expander("¿Que tipos de datos hay?"):
    st.write("Esto muestra los tipos de datos del dataset:")
    st.write (area.dtypes)    

# Esto muestra lños nombres de las columnas
with st.expander("Nombre de las columnas del Dataset"):
    st.write("Esto muestra los nombres de la columna del dataset:")
    st.write(area.columns.tolist())

# Esto muestra los valores unicos de la columna TAP
with st.expander("Valores unicos del **TAP** y su informacion"):
   with st.expander("📘 Ver significado de los valores de TAP"):
    st.write(area["tap"].unique())
    st.markdown("""
    **Valor 1 – Parque**  
    Área representativa de una región biogeográfica, de gran atractivo por su belleza o interés científico, mantenida sin otras alteraciones que las necesarias para asegurar su control, la atención al visitante y la defensa nacional.

    **Valor 2 – Reserva**  
    Área de interés para la conservación de los sistemas ecológicos, la protección de un Parque contiguo o de zonas de conservación independientes, cuando la situación existente no requiera o admita el régimen de un Parque.

    **Valor 3 – Monumento natural**  
    Área, cosa, especie viva de animal o planta, que tiene un interés estético, histórico o científico. Se la protege de manera absoluta, es inviolable, y la única actividad permitida son las inspecciones oficiales, las investigaciones y las medidas necesarias para su cuidado y atención de los visitantes.
    """)


