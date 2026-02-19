import streamlit as st
import pandas as pd
from st_aggrid import AgGrid

# Lista de dicionários simulando um banco de dados de gêneros
reviews = [
  { "id": 1, "stars": "5" },
  { "id": 2, "stars": "4" },
  { "id": 3, "stars": "3" },
]

def show_reviews():
    st.write('Lista de Avaliações')
    # Exibe a lista de gêneros em uma tabela interativa (AgGrid)
    
    AgGrid(
        data = pd.DataFrame(reviews), # Converte a lista para DataFrame do Pandas
        reload_data = True, # Garante a atualização dos dados na tela
        key = 'reviews_grid', # Chave única para o componente
        )