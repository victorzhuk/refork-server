import os
from bottle import Bottle
from bottle.ext import sqlalchemy

from .conf import db_conf


def create_app():
    app = Bottle(catchall=True)
    app.install(sqlalchemy.Plugin(
        db_conf['engine'],
        db_conf['base'].metadata,
        keyword='db',
        create=True,
        commit=True,
        use_kwargs=False
    ))
    return app
