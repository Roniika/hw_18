from typing import List
from flask import abort

from dao.model.models import Movie
from dao.movie import MovieDAO


class MovieService:

    def __init__(self, movie_dao: MovieDAO):
        self.movie_dao = movie_dao

    def get_movies(self, **params) -> List[Movie]:
        return self.movie_dao.get_all(**params)

    def get_movie(self, movie_id):
        if result := self.movie_dao.get_one_by_id(movie_id):
            return result
        abort(404)

    def create_movie(self, **data):
        return self.movie_dao.create(**data)

    def update_movie(self, movie_id, **data):
        if result := self.movie_dao.update(movie_id, **data):
            return result
        abort(404)

    def delete_movie_by_id(self, movie_id):
        if not self.movie_dao.delete(movie_id):
            abort(404)
