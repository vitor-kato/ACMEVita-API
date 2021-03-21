from .. import ma
from .models import Dependent


class DependentsSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Dependent
        exclude = ("created_at", "updated_at")
