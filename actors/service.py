from actors.repository import ActorRepository


class ActorService:

    def __init__(self):
        self.actor_repository = ActorRepository() # Instanciando minha classe

        def get_actors(self):
            return self.actor_repository.get_actors() # Retornando minha lista de atores com a função 'get_actors' de 'ActorRepository'
        

        def create_actor(self, name, birthday, nationality): # Actor existem três campos para atores
            actor = dict( # Criamos variavel que recebe um dicionario dos três campos para tratar porque repository só vai receber 'actor'
                name=name,
                birthday=birthday,
                nationality=nationality,
            )
            return self.actor_repository.create_actor(actor) # Criando o ator e passando o parametro tratado
        
            