from setup_db import db


class BaseDAO:

    def __init__(self, session):
        self.session = session
        self.model: db.Model

    def get_all(self, **params):
        query = self.model.query
        for param, value in params.items():
            if value:
                query = query.filter(getattr(self.model, param) == value)
        return query.all()

    def get_one_by_id(self, pk):
        return self.session.query(self.model).filter(self.model.id == pk).first()

    def create(self, **kwargs):
        new_item = self.model(**kwargs)
        try:
            self.session.add(new_item)
            self.session.commit()

        except Exception as e:
            print(f"Не удалось добавить новый фильм")
            self.session.rollback()

        return new_item

    def update(self, pk, **kwargs):
        if movie := self.model.query.filter_by(id=pk).first():
            [setattr(movie, attribute, value) for attribute, value in kwargs.items()]
        try:
            self.session.commit()
        except Exception as e:
            print(f"Не удалось внести изменения")
            self.session.rollback()
        return movie

    def delete(self, pk):
        try:
            result = self.session.query(self.model).filter(self.model.id == pk).delete()
            self.session.commit()
        except Exception as e:
            print(f"Не удалось удалить фильм")
            self.session.rollback()
        return result
