from flask_restx import reqparse

movie_query_parser = reqparse.RequestParser()
movie_query_parser.add_argument('director_id', type=int, help='director_id for filtering', store_missing=False)
movie_query_parser.add_argument('genre_id', type=int, help='genre_id for filtering', store_missing=False)
movie_query_parser.add_argument('year', type=int, help='year for filtering', store_missing=False)

movie_new_parser = reqparse.RequestParser()
movie_new_parser.add_argument('title', type=str, help='new movie title', required=True)
movie_new_parser.add_argument('description', type=str, help='new movie description', required=True)
movie_new_parser.add_argument('trailer', type=str, help='new movie trailer', store_missing=False)
movie_new_parser.add_argument('year', type=int, help='new movie year', required=True)
movie_new_parser.add_argument('rating', type=float, help='new movie rating', store_missing=False)
movie_new_parser.add_argument('genre_id', type=int, help='new movie genre_id', required=True)
movie_new_parser.add_argument('director_id', type=int, help='new movie director_id', required=True)


movie_update_parser = reqparse.RequestParser()
movie_update_parser.add_argument('title', type=str, help='new movie title', store_missing=False)
movie_update_parser.add_argument('description', type=str, help='new movie description', store_missing=False)
movie_update_parser.add_argument('trailer', type=str, help='new movie trailer', store_missing=False)
movie_update_parser.add_argument('year', type=int, help='new movie year', store_missing=False)
movie_update_parser.add_argument('rating', type=float, help='new movie rating', store_missing=False)
movie_update_parser.add_argument('genre_id', type=int, help='new movie genre_id', store_missing=False)
movie_update_parser.add_argument('director_id', type=int, help='new movie director_id', store_missing=False)











