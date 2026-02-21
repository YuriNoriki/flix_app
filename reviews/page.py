import streamlit as st
import pandas as pd
from st_aggrid import AgGrid
from reviews.service import ReviewService
from movies.service import MovieService


def show_reviews():
    review_service = ReviewService()
    reviews = review_service.get_reviews()
    
    if reviews:
      st.write('Lista de Avaliações')
      
      reviews_df = pd.json_normalize(reviews)
      # Exibe a lista de gêneros em uma tabela interativa (AgGrid)
      AgGrid(
          data = reviews_df, # Converte a lista para DataFrame do Pandas
          reload_data = True, # Garante a atualização dos dados na tela
          key = 'reviews_grid', # Chave única para o componente
          )
    else:
         st.warning('Nenhum filme encontrado')
    
    st.title('Cadastrar nova avaliação')

    movie_service = MovieService()
    movies = movie_service.get_movies()
    movie_titles = {movie['title'] : movie['id'] for movie in movies}
    selected_movie_title = st.selectbox('Filme', list(movie_titles.keys()))

    stars = st.number_input(
        label='Estrelas',
        min_value=0,
        max_value=5,
        step=1,
    )
    comment = st.text_area('Comentário')

    if st.button('Cadastrar'):
        new_review = review_service.create_review(
            movie=movie_titles[selected_movie_title],
            stars=stars,
            comment=comment,
        )
        if new_review:
            st.rerun()
        else:
             st.error('Error ao cadastrat o(a) Ator/Atriz, Verifique os campos.')