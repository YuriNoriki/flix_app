from movies.repository import MovieRepository

class MovieService:

    def __init__(self):
        self.movie_repository = MovieRepository()

    def get_movies(self):
        return self.movie_repository.get_movies()
    
    def create_movie(self, title,  realese_date, genre, actors, resume):
        movie = dict(
            title=title,
            realese_date=realese_date,
            genre=genre,
            actors=actors,
            resume=resume,
        )
        return self.movie_repository.create_movie(movie)
    
    def get_movie_stats(self):
        return self.movie_repository.get_movies_stats()