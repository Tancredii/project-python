from flask import Blueprint

from config import Config

bp = Blueprint('movie', __name__,
               url_prefix=f"/{Config.API_VERSION}/admin/movies")
from . import views


def init_app(app):
    app.register_blueprint(bp)