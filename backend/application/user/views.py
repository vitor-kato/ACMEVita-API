from marshmallow import ValidationError
from sqlalchemy.exc import IntegrityError

from ..base_view import BaseView
from .models import User
from .schemas import UserSchema


class UserView(BaseView):
    schema = UserSchema

    def post(self):
        super(UserView, self).post()
        try:
            data = self.get_data()
            username = data.pop("username")
            password = data.pop("password")
            user = User(username=username)
            user.hash_password(password)
            user.save()
            return self.jsonify(user), 201
        except IntegrityError:
            self.abort(400, "User already exists")
        except ValidationError as e:
            self.abort(400, e.messages)
