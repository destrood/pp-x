import streamlit as st
import pandas as pd
import plotly.express as px

# Título y encabezado
st.title("Parte 2")
st.header("Gráfico de barras que muestra la cantidad de áreas protegidas por categoría, resaltando la categoría con más zonas protegidas")

# --- Datos de ejemplo: áreas protegidas ---
data = {
    "Categoría": ["Reserva", "Parque", "Monumento Natural", "Reserva Marina", "Santuario"],
    "Cantidad": [38, 7, 2, 15, 10]
}

df = pd.DataFrame(data)

# --- Resaltar la categoría con más zonas protegidas ---
max_zonas = df["Cantidad"].max()
df["Color"] = df["Cantidad"].apply(lambda x: "red" if x == max_zonas else "blue")

# --- Gráfico de barras ---
fig = px.bar(
    df,
    x="Categoría",
    y="Cantidad",
    text="Cantidad",
    color="Color",
    color_discrete_map={"red": "red", "blue": "blue"},
    title="Cantidad de Áreas Protegidas por Categoría"
)
fig.update_traces(textposition='outside')

# --- Mostrar en Streamlit ---
st.plotly_chart(fig, use_container_width=True)
