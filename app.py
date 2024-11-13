import streamlit as st
import pandas as pd
import plotly.express as px

car_data = pd.read_csv('vehicles.csv')  # lendo os dados
# Título do webapp
st.header('Visualização de carros com maior quilometragem(tipo vs odometro)')

# Caixas de seleção para criar um histograma e gráfico de dispersão
build_hist = st.checkbox('Criar Histograma (tipo de carro vs odometro)')
build_disp = st.checkbox(
    'Criar Gráfico de Dispersão (tipo de carro vs odometro)')


if build_hist:  # se o botão for clicado
    # escrever uma mensagem
    st.write('Histograma:)')
    # criar um histograma
    fig_hist = px.histogram(car_data, x="odometer", y="type", labels={
                            'odometer': 'odometro', 'type': 'Tipo do Veículo'}, title='Tipo de Veículo vs odometro')
    # exibir um histograma Plotly interativo
    st.plotly_chart(fig_hist, use_container_width=True)


if build_disp:  # se o botão for clicado
    # escrever uma mensagem
    st.write('Gráfico de Dispersão: (Tipo vs Odometro)')
    # criar um gráfico de dispersão
    fig_disp = px.scatter(car_data, x="odometer", y="type", labels={
                          'odometer': 'odômetro', 'type': 'Tipo do Veículo'}, title='Tipo de Veículo vs odometro')
    # exibir um gráfico de dispersão Plotly interativo
    st.plotly_chart(fig_disp, use_container_width=True)

# Fim do Código
