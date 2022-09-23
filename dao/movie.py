from dao.base import BaseDAO
from dao.model.models import Movie


class MovieDAO(BaseDAO):
    def __init__(self, session):
        self.session = session
        self.model = Movie







