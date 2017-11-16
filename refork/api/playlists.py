from bottle import request, abort

from ..core import create_app

api = create_app()


@api.get('/')
def get_playlists():
    return {'success': True}
