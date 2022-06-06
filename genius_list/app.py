from flask import Flask
from genius_list.blueprints import restapi
from genius_list.ext import cache


def create_app(**config):
    app = Flask(__name__)
    restapi.init_app(app)
    cache.init_app(app)
    print("test")
    return app
