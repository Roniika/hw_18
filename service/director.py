from typing import List
from flask import abort

from dao.director import DirectorDAO
from dao.model.models import Director


class DirectorService:

    def __init__(self, director_dao: DirectorDAO):
        self.director_dao = director_dao

    def get_directors(self) -> List[Director]:
        return self.director_dao.get_all()

    def get_director(self, did):
        if result := self.director_dao.get_one_by_id(did):
            return result
        abort(404)
