from genres.repository import GenreRepository
import streamlit as st

class GenresService: # Define a classe de Serviço (contém a lógica de negócio)
    
    def __init__(self):
        # Ao iniciar, cria uma instância do Repositório para poder usar seus métodos
        self.genre_repository = GenreRepository()

    def get_genres(self):
        if 'genres' in st.session_state:
            return st.session_state.genres
        genres = self.genre_repository.get_genres()
        st.session_state.genres = genres
        return genres
    
    def create_genre(self, name):
        # Cria um dicionário com os dados do gênero (prepara o objeto para a API)
        genre = dict(
            name=name,
        )
        new_genre = self.genre_repository.create_genre(genre)
        st.session_state.genres.append(new_genre)
        # Envia o dicionário para o repositório realizar a gravação (POST) na API
        return new_genre