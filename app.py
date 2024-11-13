import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')  # lendo os dados
# Título do webapp
st.header('Header teste, atualizar depois de entender onde isso vai kkk')

# Caixas de seleção para criar um histograma e gráfico de dispersão
build_hist = st.checkbox('Criar Histograma')
build_disp = st.checkbox('Criar Gráfico de Dispersão')


if build_hist:  # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um histograma...')

if build_disp:  # se o botão for clicado
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão...')

# criar um histograma
fig_hist = px.histogram(car_data, x="odometer")
# criar um gráfico de dispersão
fig_disp = px.scatter(car_data, x="odometer", y="price")

# exibir um gráfico Plotly interativo
st.plotly_chart(fig_hist, use_container_width=True)
st.plotly_chart(fig_disp, use_container_width=True)


# Lembrar de atualizar o README.txt com resumo do projeto
