import streamlit as st
import requests
from login.service import logout

class GenreRepository:

    def __init__(self):
        self.__base_url = "http://127.0.0.1:8000/api/v1/" # URL raiz da API
        self.__genres_url = f'{self.__base_url}genres/' # URL específica para o recurso de gêneros
        self.__headers = {
            'Authorization' : f'Bearer {st.session_state.token}' # Define os cabeçalhos da requisição incluindo o Token de autenticação
        }

    def get_genres(self):
        response = requests.get( # Faz uma requisição GET enviando o token nos headers para autorização
            self.__genres_url,
            headers=self.__headers,
        )
        if response.status_code == 200:
            return response.json()
        if response.status_code  == 401:
            logout()
            return None
        raise Exception(f' Error ao obter dados da API. Status code {response.status_code}')
    
    def create_genre(self, genre):
        response = requests.post(
            self.__genres_url,
            headers=self.__headers,
            data=genre,
        )
        if response.status_code == 201:
            return response.json()
        if response.status_code  == 401:
            logout()
            return None
        raise Exception(f' Error ao obter dados da API. Status code {response.status_code}')
    