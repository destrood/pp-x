import folium
import streamlit as st
from streamlit_folium import folium_static, st_folium
import pandas as pd

def generar_mapa():
    attr = (
        '&copy; <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> '
        'contributors, &copy; <a href="https://cartodb.com/attributions">CartoDB</a>'
    )
    
    tiles = 'https://wms.ign.gob.ar/geoserver/gwc/service/tms/1.0.0/capabaseargenmap@EPSG%3A3857@png/{z}/{x}/{-y}.png'
    m = folium.Map(
        location=(-33.457606, -65.346857),
        control_scale=True,
        zoom_start=5,
        name='es',
        tiles=tiles,
        attr=attr
    )
    return m


lagos = pd.read_csv('area_protegida.csv')
import streamlit as st
st.markdown("#  Mapa de Áreas Protegidas de Argentina")
st.caption("Fuente: Catálogo de objetos geográficos IGN – Clasificación TAP: Parque, Reserva y Monumento Natural.")

mapa = generar_mapa()

def agregar_marca_aerop(row):
    
    #st.write(color)
    folium.Marker(
        [row['lat'], row['lng']],
        popup=row['tap'],
        icon=folium.Icon()
        ).add_to(mapa)

ac1,ac2 = st.columns([0.3, 0.7])
r_parques = ac1.checkbox("reserva")
if r_parques:
    a_med = lagos[lagos['tap']== 2]
    a_med.apply(agregar_marca_aerop, axis=1)
r_areas = ac1.checkbox("Parque")
if r_areas:
    a_larg = lagos[lagos['tap']== 1]
    a_larg.apply(agregar_marca_aerop, axis=1)
r_monu = ac1.checkbox("Monumento")
if r_monu:
    a_small = lagos[lagos['tap']== 3]
    a_small.apply(agregar_marca_aerop, axis=1)
with ac2:
    st_folium(mapa, key='area')
