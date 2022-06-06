from flask_restful import Resource, request
from .services import search_artist
from genius_list.ext.cache import cache


class GeniusResource(Resource):

    @cache.cached(timeout=86400 * 7)
    def get(self, artist_name):
        query_cache = request.args.get('cache', None)
        if query_cache is not None and query_cache.lower() == 'false':
            cache.clear()

        return search_artist(artist_name), 200
