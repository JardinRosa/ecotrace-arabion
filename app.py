"""

============
EcoTrace AI|
============

console:  python -m streamlit run app.py
"""

import pandas as pd
import streamlit as st

st.set_page_config(page_title="EcoTrace", page_icon="🚗", layout="wide")

# lateral
precios = pd.read_csv("data/precios.csv")
gas91 = precios[precios["combustible"] == "gasolina_91"].iloc[0]

st.sidebar.title("EcoTrace AI")
st.sidebar.metric("Gasolina 91 (Panamá y Colón)", f"B/. {gas91['precio_litro']:.3f} por litro")
st.sidebar.caption(f"Vigente del {gas91['vigente_desde']} al {gas91['vigente_hasta']} · Secretaría Nacional de Energía")

# header
st.title("¿Cuánto te cuesta tu carro al mes?")
st.write("Calcula el costo en combustible y el CO₂ de tu carro para ir al trabajo, con datos oficiales.")

# tabs
tab_catalogo, tab_gasto, tab_comparar, tab_otro, tab_ranking, tab_estadisticas = st.tabs(
    ["Catálogo", "Mi gasto", "Comparar", "Otro modelo", "Ranking", "Estadísticas"]
)

# Pendientes del equipo: 

with tab_catalogo:
    st.subheader("Modelos que se venden en Panamá")
    st.info("Pendiente: tabla del catálogo (datos.crear_catalogo).")

with tab_gasto:
    st.subheader("Calcula tu gasto del mes")
    st.info("Pendiente: elegir modelo, km por día y días al mes (calculos.resumen).")

with tab_comparar:
    st.subheader("Compara dos modelos")
    st.info("Pendiente: dos modelos y el ahorro (calculos.comparar).")

with tab_otro:
    st.subheader("¿Tu carro no está en el catálogo?")
    st.info("Pendiente: km por litro y combustible (calculos.kml_a_l100).")

with tab_ranking:
    st.subheader("Del más barato al más caro de mantener")
    st.info("Pendiente: tabla, gráfico de barras y botón de descarga (reportes.ranking).")

with tab_estadisticas:
    st.subheader("Lo que dicen los datos")
    st.info("Pendiente: promedio, mediana, correlación y gráfico motor vs. consumo (reportes.estadisticas).")