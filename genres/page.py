import streamlit as st


genres = [
  { "id": 1, "nome": "Ação" },
  { "id": 2, "nome": "Drama" },
  { "id": 3, "nome": "Comédia" }
]


def show_genres():
    st.write('Lista de gêneros')
    
    st.table(genres)

    st.title('Cadastrar novo gênero')
    name = st.text_input('Nome do Gênero')
   
    if st.button('Cadastrar'):
        st.success(f'Gênero "{name}" cadastrado com sucesso')