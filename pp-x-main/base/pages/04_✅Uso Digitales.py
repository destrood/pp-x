import pandas as pd
import streamlit as st
import plotly.express as px

uso = pd.read_csv('uso_digitales_FINAL.csv')

st.markdown("#  Análisis de las Redes Sociales Más Utilizadas Basado en Datos Reales")

with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = uso.shape
    st.write(f'Tiene { filas} filas y {columnas} columnas')

with st.expander("Nombre de las columnas del dataset"):
    st.write(uso.columns.tolist())

#Esto mostrara los tipo de datos

with st.expander("¿Que tipos de datos hay?"):
    st.write("Esto muestra los tipos de datos del dataset:")
    st.write (uso.dtypes)   

st.header("Se usó la columna “Marca temporal” para analizar la distribución de las encuestas y crear gráficos interactivos con Plotly en Streamlit, mostrando claramente la cantidad de registros a lo largo del año 2024.")

uso["Marca temporal"] = pd.to_datetime(
    uso["Marca temporal"],
)
# EL dt.to_period se usa para convertir una serie de fechas en una serie de periodos como por ejemplo dia,mes,año.

uso["Mes"] = uso["Marca temporal"].dt.to_period("M").astype(str)

fig = px.histogram(
    uso,
    x="Mes",
    title="Cantidad de encuestas por mes"
)

st.plotly_chart(fig, use_container_width=True)

