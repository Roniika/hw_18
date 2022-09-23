from dao.model.models import Director
from .base import BaseDAO


class DirectorDAO(BaseDAO):
    def __init__(self, session):
        self.session = session
        self.model = Director

