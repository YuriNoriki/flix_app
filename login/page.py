import streamlit as st
from login.service import login

def show_login(): # Define a função que desenha a tela de login na interface
    st.title('Login') # Exibe um título grande no topo da página

    username = st.text_input('Usuário') # Cria um campo de entrada de texto para o nome do usuário
    password = st.text_input( # Cria um campo de entrada para a senha
        label= 'Senha', # Rótulo que aparece acima do campo
        type= 'password' # Mascara os caracteres digitados (exibe bolinhas)
    )

    if st.button('Login'): # Cria um botão "Login" e verifica se ele foi clicado
    # Chama a função login (service.py) passando os dados digitados
        login(
            username= username,
            password= password,
        )