import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


# Lista de dicionários simulando um banco de dados de gêneros
genres = [
  { "id": 1, "nome": "Ação" },
  { "id": 2, "nome": "Drama" },
  { "id": 3, "nome": "Comédia" }
]


def show_genres():
    st.write('Lista de gêneros')
    # Exibe a lista de gêneros em uma tabela interativa (AgGrid)
    
    AgGrid(
        data = pd.DataFrame(genres), # Converte a lista para DataFrame do Pandas
        reload_data = True, # Garante a atualização dos dados na tela
        key = 'genres_grid', # Chave única para o componente
        )

    # Campo de entrada de texto para o nome do novo gênero
    st.title('Cadastrar novo gênero')
    name = st.text_input('Nome do Gênero')
   
   # Lógica executada ao clicar no botão de cadastro
    if st.button('Cadastrar'):
        # Exibe mensagem de sucesso (apenas visual neste estágio)
        st.success(f'Gênero "{name}" cadastrado com sucesso')