import requests


class Auth(): # Define a classe responsável pela autenticação
    
    def __init__(self): # Método construtor executado ao instanciar a classe
       self.__base_url = "..." # Define a URL base da API (atributo privado)
       self.__auth_url = f'{self.__base_url}authentication/token/' # Monta o endpoint específico de token
    
    def get_token(self, username, password): # Método para obter o token de acesso

# Cria o dicionário com as credenciais para o corpo da requisição
        auth_payload = {
            'username' : username,
            'password' : password,
        }

# Realiza a requisição POST enviando os dados (form-data)
        auth_response = requests.post(
            self.__auth_url,
            data= auth_payload 
        )

# Verifica se o login foi bem-sucedido (Status 200)
        if auth_response.status_code == 200:
            return auth_response.json() # Retorna o corpo da resposta em formato de dicionário

# Retorna um dicionário de erro caso a autenticação falhe
        return {'error': f'Error ao authenticar. Status code: {auth_response.status_code}'}