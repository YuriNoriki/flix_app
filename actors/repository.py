import streamlit as st
import requests
from login.service import logout


class ActorRepository:

    def __init__(self):
        self.__base_url = 'http://127.0.0.1:8000/api/v1/' # URL raiz da API
        self.__actors_url = f'{self.__base_url}actors/'
        self.__headers = {
            'Authorization' : f'Bearer {st.session_state.token}'
        }

    def get_actors(self):
        response = requests.get(
            self.__actors_url,
            headers=self.__headers,
        )
        if response == 200:
            return response.json()
        if response == 400:
            logout()
            return None
        raise Exception(f' Error ao obter dados da API. Status code {response.status_code}')
        

    def create_actor(self, actor):
        response = requests.post(
            self._actors_url,
            headers=self.__headers,
            data=actor,
        )
        if response == 201:
                return response.json()
        if response == 401:
            logout()
            return None
        raise Exception(f' Error ao obter dados da API. Status code {response.status_code}')