from flask import Blueprint

from . import models, schemas

department_bp = Blueprint("department", __name__)
