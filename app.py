import pandas as pd
import plotly.express as px
import streamlit as st

st.header('Panel de anuncios de venta de coches')

car_data = pd.read_csv('vehicles_us.csv')

build_histogram = st.checkbox('Construir un histograma')
if build_histogram:
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    fig = px.histogram(car_data, x="odometer", title="Distribución del odómetro")
    st.plotly_chart(fig, use_container_width=True)

build_scatter = st.checkbox('Construir un gráfico de dispersión')
if build_scatter:
    st.write('Creación de un gráfico de dispersión: odómetro vs. precio')
    fig_scatter = px.scatter(car_data, x="odometer", y="price", title="Relación entre odómetro y precio")
    st.plotly_chart(fig_scatter, use_container_width=True)
