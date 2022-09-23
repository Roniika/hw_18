from flask_restx import Resource, Namespace, fields

from implemented import genre_service


genre_ns = Namespace('genres')


genre_model = genre_ns.model('genre', {
    'id': fields.Integer(readonly=True, discription='genre id'),
    'name': fields.String(required=True, discription='genre name')
})


@genre_ns.route('/')
class GenresView(Resource):
    @genre_ns.marshal_list_with(genre_model)
    @genre_ns.response(200, 'OK')
    def get(self):
        return genre_service.get_genres(), 200


@genre_ns.route('/<int:genre_id>')
class GenresView(Resource):
    @genre_ns.marshal_with(genre_model)
    @genre_ns.response(200, 'OK')
    @genre_ns.response(404, 'Not found')
    def get(self, genre_id: int):
        return genre_service.get_genre(genre_id), 200