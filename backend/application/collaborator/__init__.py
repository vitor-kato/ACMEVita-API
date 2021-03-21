from flask import Blueprint

from . import models, schemas

collaborator_bp = Blueprint("collaborator", __name__)
