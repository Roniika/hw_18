from flask_restx import Resource, Namespace, fields

from implemented import director_service

director_ns = Namespace('directors')


director_model = director_ns.model('director', {
    'id': fields.Integer(readonly=True, discription='director id'),
    'name': fields.String(required=True, discription='director name')
})

@director_ns.route('/')
class DirectorsView(Resource):
    @director_ns.marshal_list_with(director_model)
    @director_ns.response(200, 'OK')
    def get(self):
        return director_service.get_directors(), 200


@director_ns.route('/<int:director_id>')
class DirectorView(Resource):
    @director_ns.marshal_with(director_model)
    @director_ns.response(200, 'OK')
    @director_ns.response(404, 'Not found')
    def get(self, director_id: int):
        return director_service.get_director(director_id), 200

