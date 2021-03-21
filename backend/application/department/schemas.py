from .. import ma
from .models import Department


class DepartmentSchema(ma.SQLAlchemyAutoSchema):
    collaborators = ma.Nested("CollaboratorSchema", many=True)

    class Meta:
        model = Department
        exclude = ("created_at", "updated_at")
