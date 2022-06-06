from flask import Blueprint
from flask_restful import Api

from .resource import GeniusResource

bp = Blueprint("restapi", __name__, url_prefix="/api/v1")
api = Api(bp)


def init_app(app):
    api.add_resource(GeniusResource, "/artists/<artist_name>")
    app.register_blueprint(bp)
