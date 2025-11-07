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
    st.write("Esto muestra llos nombres de la columna del dataset:")
    st.write(area.columns.tolist())


