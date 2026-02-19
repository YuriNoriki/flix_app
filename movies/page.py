import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

# Lista de dicionários simulando um banco de dados de gêneros
movies = [
  { "id": 1, "name": "Ultimo azul" },
  { "id": 2, "name": "O Agente" },
  { "id": 3, "name": "O palhaço" },
]

def show_movies():
    st.write('Lista de Filmes')
    # Exibe a lista de gêneros em uma tabela interativa (AgGrid)
    
    AgGrid(
        data = pd.DataFrame(movies), # Converte a lista para DataFrame do Pandas
        reload_data = True, # Garante a atualização dos dados na tela
        key = 'movies_grid', # Chave única para o componente
        )