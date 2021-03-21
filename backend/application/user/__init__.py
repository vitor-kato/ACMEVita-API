from flask import Blueprint

from . import auth, models, schemas

user_bp = Blueprint("user", __name__)
