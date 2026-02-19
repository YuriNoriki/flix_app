import streamlit as st
from api.service import Auth

def login(username, password): # Define a função que processa a tentativa de login
    
    auth_service = Auth() # Instancia a classe de autenticação

# Chama o método get_token passando as credenciais do formulário
    response = auth_service.get_token(
        username= username,
        password= password,
    )

# Verifica se o dicionário de resposta contém a chave 'error'
    if response.get('error'):
    # Exibe um alerta visual vermelho na interface do Streamlit com o erro
        st.error(f'Falha ao realizar login: {response.get("error")}')
    else:
    # Armazena o token recebido no estado da sessão (persiste entre reloads)
        st.session_state.token = response.get('access')
    # Reinicia o app para atualizar a interface já com o usuário logado
        st.rerun()