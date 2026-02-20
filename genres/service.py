from genres.repository import GenreRepository

class GenresService: # Define a classe de Serviço (contém a lógica de negócio)
    
    def __init__(self):
        # Ao iniciar, cria uma instância do Repositório para poder usar seus métodos
        self.genre_repository = GenreRepository()

    def get_genres(self):
        # Apenas repassa a ordem para o repositório buscar a lista de gêneros
        return self.genre_repository.get_genres()
    
    def create_genre(self, name):
        # Cria um dicionário com os dados do gênero (prepara o objeto para a API)
        genre = dict(
            name=name,
        )
        # Envia o dicionário para o repositório realizar a gravação (POST) na API
        return self.genre_repository.create_genre(genre)