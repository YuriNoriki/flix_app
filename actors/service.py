from actors.repository import ActorRepository
import streamlit as st


class ActorService:

    def __init__(self):
        self.actor_repository = ActorRepository() # Instanciando minha classe

    def get_actors(self):
        if 'actors' in st.session_state: # 1. Verifica se a lista de atores já existe no estado da sessão do Streamlit
            return st.session_state.actors # Se existir, retorna os dados salvos (evita ir ao banco/API novamente)
        actors = self.actor_repository.get_actors() # 2. Se não existir, busca os dados através do repositório (chamada à API)
        st.session_state.actors = actors # 3. Salva os dados obtidos no session_state para uso futuro na sessão
        return actors # 4. Retorna a lista obtida da API
        
    def create_actor(self, name, birthday, nationality): # Actor existem três campos para atores
        actor = dict( # 1. Empacota os dados em um dicionário para enviar à API
            name= name,
            birthday= birthday,
            nationality= nationality,
        )
        new_actor = self.actor_repository.create_actor(actor) # 2. Chama o repositório para persistir os dados no banco via API
        # 3. Atualiza o cache local (session_state) para que a lista exibida
    #    na tela reflita o novo ator sem precisar recarregar tudo
        st.session_state.actors.append(new_actor)
        # 4. Retorna o objeto criado para confirmação
        return new_actor
        
            