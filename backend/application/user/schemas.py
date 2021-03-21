from .. import ma
from .models import User


class UserSchema(ma.SQLAlchemyAutoSchema):
    password = ma.String(required=True, load_only=True)

    class Meta:
        model = User
        exclude = ("created_at", "updated_at", "password_hash")
