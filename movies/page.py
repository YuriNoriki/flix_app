import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid
from movies.service import MovieService
from actors.service import ActorService
from genres.service import GenresService


def show_movies():
    movie_service = MovieService()
    movies = movie_service.get_movies()

    if movies:
      st.write('Lista de Filmes')
      # Exibe a lista de gêneros em uma tabela interativa (AgGrid)
      
      movies_df = pd.json_normalize(movies)
      movies_df = movies_df.drop(columns=['actors', 'genre.id']) # Fazendo tratamento de daodos

      AgGrid(
          data=movies_df, # Converte a lista para DataFrame do Pandas
          reload_data=True, # Garante a atualização dos dados na tela
          key = 'movies_grid', # Chave única para o componente
        )
    else:
       st.warning('Nenhum filme encontrado')

    st.title('Cadastrar Novo Filme')

    title = st.text_input('Título')

    realese_date = st.date_input( # Campo para colocar os dados de aniversario
        label= 'Data do Lançamento', # Título que aparece acima do campo
        value= datetime.today(), # Define a data inicial como "hoje"
        min_value= datetime(1800, 1, 1).date(), # Impede datas anteriores a 1600
        max_value=datetime.today(), # Impede selecionar qualquer dia no futuro
        format='DD/MM/YYYY', # Define como o usuário vê a data (padrão brasileiro)
    )

    genre_service = GenresService()
    genres = genre_service.get_genres() # buscando todos os generos cadastrados
    genre_names = {genre['name']: genre['id'] for genre in genres}
    selected_genre_name = st.selectbox('Gênero', list(genre_names.keys()))

    actor_service = ActorService()
    actors = actor_service.get_actors()
    actor_names = {actor['name']: actor['id'] for actor in actors}
    selected_actors_names = st.multiselect('Atores/Atrizes', list(actor_names.keys()))
    selected_actors_ids = [actor_names[name] for name in selected_actors_names]

    resume = st.text_area('Resumo')

    if st.button('Cadastrar'):
        new_movie = movie_service.create_movie(
          title=title,
          realese_date= realese_date,
          genre= genre_names[selected_genre_name],
          actors=selected_actors_ids,
          resume=resume,
       )
        if new_movie:
          st.rerun()
        else:
          st.error('Error ao cadastrat o(a) Ator/Atriz, Verifique os campos.')