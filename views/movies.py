from flask_restx import Resource, Namespace, fields
from .parsers import movie_query_parser, movie_new_parser, movie_update_parser
from .directors import director_model
from .genres import genre_model
from implemented import movie_service


movie_ns = Namespace('movies')


movie_model = movie_ns.model('movie', {
    'id': fields.Integer(readonly=True, discription='movie id'),
    'title': fields.String(required=True, discription='movie title'),
    'description': fields.String(required=True, discription='movie description'),
    'trailer': fields.String(required=True, discription='movie trailer'),
    'year': fields.Integer(required=True, discription='movie year'),
    'rating':fields.Float(required=True, discription='movie rating'),
    'genre_id': fields.Integer(required=True, discription='movie genre_id'),
    'director_id': fields.Integer(required=True, discription='movie director_id'),
    'genre': fields.Nested(genre_model, required=True, discription='genre object'),
    'director': fields.Nested(director_model, required=True, discription='director object')
})


@movie_ns.route('/')
class MoviesView(Resource):
    @movie_ns.marshal_list_with(movie_model)
    @movie_ns.response(200, 'All ok')
    @movie_ns.expect(movie_query_parser)
    def get(self):
        params = movie_query_parser.parse_args()
        return movie_service.get_movies(**params)

    @movie_ns.marshal_with(movie_model, code=201)
    @movie_ns.response(201, 'Correct')
    @movie_ns.response(400, 'Invalid data')
    @movie_ns.expect(movie_new_parser)
    def post(self):
        data = movie_new_parser.parse_args()
        return movie_service.create_movie(**data), 201


@movie_ns.route('/<int:movie_id>')
class MovieView(Resource):
    @movie_ns.marshal_with(movie_model)
    @movie_ns.response(200, 'Correct')
    @movie_ns.response(404, 'Not found')
    def get(self, movie_id: int):
        return movie_service.get_movie(movie_id)

    @movie_ns.marshal_with(movie_model, code=201)
    @movie_ns.response(201, 'Correct')
    @movie_ns.response(404, 'Not found')
    @movie_ns.expect(movie_update_parser)
    def put(self, movie_id: int):
        data = movie_update_parser.parse_args()
        return movie_service.update_movie(movie_id, **data), 201

    @movie_ns.response(204, 'OK')
    @movie_ns.response(404, 'Not found')
    def delete(self, movie_id: int):
        return movie_service.delete_movie_by_id(movie_id), 204