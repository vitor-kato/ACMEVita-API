from flask import Blueprint

from . import models, schemas

dependent_bp = Blueprint("dependent", __name__)
