import sys
from bottle import run

from refork.app import main_app

wsgi = main_app

if __name__ == '__main__':
    run(wsgi, host='127.0.0.1', port=5000, debug=True, reloader=True)
