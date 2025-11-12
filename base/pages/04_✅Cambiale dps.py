import pandas as pd
import streamlit as st
import plotly.express as px

uso = pd.read_csv('uso_digitales_FINAL.csv')

st.markdown("#  Análisis de las Redes Sociales Más Utilizadas Basado en Datos Reales")

with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = uso.shape
    st.write(f'Tiene { filas} filas y {columnas} columnas')

with st.expander("Nombre de las columnas dedl dataset"):
    st.write(uso.columns.tolist())

with st.expander("¿Cuántas filas y columnas tiene el dataset?"):
    filas, columnas = uso.shape
    st.write(f'Tiene { filas} filas y {columnas} columnas')


st.markdown("Análisis de las Redes Sociales Más Utilizadas Basado en Datos Reales")

# Cargar datos
df = pd.read_csv("uso_digitales_FINAL.csv")

uso_redes = {
    "Instagram": df["instagram"].notna().sum(),
    "TikTok": df["tiktok"].notna().sum(),
    "YouTube": df["youtube"].notna().sum(),
    "Twitter (X)": df["twiter"].notna().sum(),
}

df_redes = pd.DataFrame(list(uso_redes.items()), columns=["Red Social", "Usuarios"])


fig = px.bar(
    df_redes,
    x="Red Social",
    y="Usuarios",
    color="Red Social",
    title="Uso de Redes Sociales entre los participantes",
    text="Usuarios",
)

# Mostrar gráfico
st.plotly_chart(fig)
