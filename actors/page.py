import streamlit as st
import pandas as pd
from st_aggrid import AgGrid


# Lista de dicionários simulando um banco de dados de gêneros
actors = [
  { "id": 1, "name": "Wagner Moura" },
  { "id": 2, "name": "Selton Mello" },
  { "id": 3, "name": "Rodrigo Santoro" },
]


def show_actors():
    st.write('Lista de Atores/Atriz')
    # Exibe a lista de gêneros em uma tabela interativa (AgGrid)
    
    AgGrid(
        data = pd.DataFrame(actors), # Converte a lista para DataFrame do Pandas
        reload_data = True, # Garante a atualização dos dados na tela
        key = 'actors_grid', # Chave única para o componente
        )
    
    # Campo de entrada de texto para o nome do novo gênero
    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do Ator/Atriz')
   
   # Lógica executada ao clicar no botão de cadastro
    if st.button('Cadastrar'):
        # Exibe mensagem de sucesso (apenas visual neste estágio)
        st.success(f'Ator/Atriz "{name}" cadastrado com sucesso')