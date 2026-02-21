# Importa a biblioteca Streamlit
# Streamlit é um framework para criar aplicações web com Python de forma simples
import streamlit as st
from genres.page import show_genres
from actors.page import show_actors
from movies.page import show_movies
from reviews.page import show_reviews
from login.page import show_login
from home.page import show_home


# Função principal da aplicação
# Boa prática: organizar o app dentro de uma função main()
def main():
    # Verifica se a chave 'token' NÃO existe no estado da sessão (usuário não logado)
    if 'token' not in st.session_state:
        show_login() # Se não existir, exibe o formulário de login na tela
    
    else:
        # Define o título principal da página
        # st.title() renderiza um <h1> na interface
        st.title('Flix App')

        # Cria um selectbox na sidebar (menu lateral)
        # st.sidebar permite criar elementos na barra lateral
        # selectbox cria um menu suspenso com opções
        menu_option = st.sidebar.selectbox(
            'Selecione uma opção',  # Texto exibido acima do selectbox
            ['Inicio', 'Gêneros', 'Atores/Atrizes', 'Filmes', 'Avaliações']  # Lista de opções
        )

        # Estrutura condicional para controlar o que aparece na tela
        # Dependendo da opção escolhida no menu, o conteúdo muda

        if menu_option == "Inicio":
           show_home()

        if menu_option == 'Gêneros':
            show_genres()

        if menu_option == 'Atores/Atrizes':  
            show_actors()

        if menu_option == 'Filmes':
            show_movies()
        
        if menu_option == 'Avaliações': 
            show_reviews()

# Verifica se o arquivo está sendo executado diretamente
# Evita que o código rode automaticamente se for importado como módulo
if __name__ == '__main__':
    main()
