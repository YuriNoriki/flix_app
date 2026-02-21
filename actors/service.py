from actors.repository import ActorRepository
import streamlit as st


class ActorService:

    def __init__(self):
        self.actor_repository = ActorRepository() # Instanciando minha classe

    def get_actors(self):
        if 'actors' in st.session_state:
            return st.session_state.actors
        actors = self.actor_repository.get_actors()
        return actors
        
    def create_actor(self, name, birthday, nationality): # Actor existem três campos para atores
        actor = dict( # Criamos variavel que recebe um dicionario dos três campos para tratar porque repository só vai receber 'actor'
            name= name,
            birthday= birthday,
            nationality= nationality,
        )
        new_actor = self.actor_repository.create_actor(actor)
        st.session_state.actors.append(new_actor)
        return new_actor
        
            