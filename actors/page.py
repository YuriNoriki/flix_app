import streamlit as st
import pandas as pd
from datetime import datetime
from st_aggrid import AgGrid
from actors.service import ActorService


def show_actors():
    actor_service = ActorService() # Instanciando a classe ActorService
    actors = actor_service.get_actors() # Traz a lista de todos atores

    if actors: # Se tiver algum ator,vai mostrar a tabela de atores
        st.write('Lista de Atores/Atriz')
        actors_df = pd.json_normalize(actors) # Fazendo um tratamento de dados pois 'actors=chave/valor' e precisamos transformar em tabela

        AgGrid(  # Exibe a lista de gêneros em uma tabela interativa (AgGrid)
            data = actors_df, # Converte a lista para DataFrame do Pandas
            reload_data = True, # Garante a atualização dos dados na tela
            key = 'actors_grid', # Chave única para o componente
        )
    else:
        st.warning('Nenhum ator/atriz foi encontrado')


    # Campo de entrada de texto para o nome do novo gênero
    st.title('Cadastrar novo Ator/Atriz')
    name = st.text_input('Nome do Ator/Atriz') # Colocar o nome no campo
    birthday = st.date_input( # Campo para colocar os dados de aniversario
        label= 'Data de Nascimento', # Título que aparece acima do campo
        value= datetime.today(), # Define a data inicial como "hoje"
        min_value= datetime(1600, 1, 1).date(), # Impede datas anteriores a 1600
        max_value=datetime.today(), # Impede selecionar qualquer dia no futuro
        format='DD/MM/YYYY', # Define como o usuário vê a data (padrão brasileiro)
    )
    nationality_dropdown = ['BR', 'USA']
    nationality = st.selectbox(
        label='Nacionalidade',
        options=nationality_dropdown,
    )

   # Lógica executada ao clicar no botão de cadastro
    if st.button('Cadastrar'):
        new_actor = actor_service.create_actor(
            name=name,
            birthday=birthday,
            nationality=nationality,
        )
        if new_actor:
            st.rerun()
        else:
            st.error('Error ao cadastrat o(a) Ator/Atriz, Verifique os campos.')