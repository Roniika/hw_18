from dao.model.models import Genre
from .base import BaseDAO


class GenreDAO(BaseDAO):
    def __init__(self, session):
        self.session = session
        self.model = Genre
