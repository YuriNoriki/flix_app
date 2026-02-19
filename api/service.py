import requests


class Auth():
    
    def __init__(self):
       self.__base_url = "..."
       self.__auth_url = f'{self.__base_url}authentication/token/' 
    
    def get_token(self, username, password):
        
        auth_payload = {
            'username' : username,
            'password' : password,
        }

        auth_response = requests.post(
            self.__auth_url,
            data= auth_payload 
        )

        if auth_payload.status_code == 200:
            return auth_response.json()
        
        return {'Error': f'Error ao authenticar. Status code: {auth_response.status_code}'}