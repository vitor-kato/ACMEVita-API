from .. import ma
from .models import Collaborator


class CollaboratorSchema(ma.SQLAlchemyAutoSchema):
    have_dependents = ma.Method("get_have_dependents", dump_only=True)
    department = ma.Str(required=True)

    class Meta:
        model = Collaborator
        exclude = ("created_at", "updated_at")

    def get_have_dependents(self, obj):
        return obj.have_dependents
