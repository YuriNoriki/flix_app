# Importa a biblioteca Streamlit
# Streamlit é um framework para criar aplicações web com Python de forma simples
import streamlit as st
from genres.page import show_genres


# Função principal da aplicação
# Boa prática: organizar o app dentro de uma função main()
def main():

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
        st.write('Inicio')

    if menu_option == 'Gêneros':
        show_genres()

    if menu_option == 'Atores/Atrizes':  
        st.write('Lista Atores/Atrizes')

    if menu_option == 'Filmes':
        st.write('Lista de Filmes')
    
    if menu_option == 'Avaliações': 
        st.write('Lista de Avalição')


# Verifica se o arquivo está sendo executado diretamente
# Evita que o código rode automaticamente se for importado como módulo
if __name__ == '__main__':
    main()
