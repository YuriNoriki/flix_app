import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from genres.service import GenresService


def show_genres():
    genres_service = GenresService() # Instancia o serviço responsável pelas operações de gênero
    genres = genres_service.get_genres() # Busca os dados de gêneros através do serviço

    if genres: # Verifica se a lista de gêneros não está vazia (ajustado de genres() para genres)
        st.write('Lista de gêneros')
        genres_df = pd.json_normalize(genres) # Converte a lista de dicionários/JSON para um DataFrame do Pandas
        AgGrid(  # Exibe a lista de gêneros em uma tabela interativa (AgGrid)
            data = genres_df, # Converte a lista para DataFrame do Pandas
            reload_data = True, # Garante a atualização dos dados na tela
            key = 'genres_grid', # Chave única para o componente
            )
    else:
        st.warning('Nenhum gênero encontrado.')

    # Campo de entrada de texto para o nome do novo gênero
    st.title('Cadastrar novo gênero')
    name = st.text_input('Nome do Gênero')
   
   # Lógica executada ao clicar no botão de cadastro
    if st.button('Cadastrar'):
        new_genre = genres_service.create_genre( # Chama o serviço para criar o gênero com o nome inserido
            name=name,
        )
        if new_genre:
            st.success('Gênero cadastrado com sucesso')
            st.rerun() # Recarrega a página para atualizar a tabela
        else:
            st.error('Erro ao cadastrar o gênero. Verifique os campos')