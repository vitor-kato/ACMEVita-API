import os

from flask import Blueprint, Flask
from flask_httpauth import HTTPBasicAuth
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy

# Globally accessible libraries
db = SQLAlchemy()
ma = Marshmallow()
api_bp = Blueprint("api", __name__, url_prefix="/api")
api = Api(api_bp)
auth = HTTPBasicAuth()


def init_app():
    """Initialize the core application."""
    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(os.environ["APP_SETTINGS"])

    # Initialize Plugins
    db.init_app(app)
    ma.init_app(app)

    with app.app_context():
        return app
