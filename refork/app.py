from bottle import mount, default_app

from .api import playlists_api


VERSION = 'v0.9.0'

main_app = default_app()

main_app.mount('/api/{0}/playlists'.format(VERSION), playlists_api, skip=None)
