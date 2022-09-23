from typing import List
from flask import abort

from dao.genre import GenreDAO
from dao.model.models import Genre


class GenreService:

    def __init__(self, genre_dao: GenreDAO):
        self.genre_dao = genre_dao

    def get_genres(self) -> List[Genre]:
        return self.genre_dao.get_all()

    def get_genre(self, genre_id):
        if result := self.genre_dao.get_one_by_id(genre_id):
            return result
        abort(404)


