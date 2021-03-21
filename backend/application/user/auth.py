from typing import AnyStr

from flask import g

from .. import auth
from .models import User


@auth.verify_password
def verify_password(username_or_token: AnyStr, password: AnyStr) -> bool:
    """Verifies if a password or a token are valid
    utilizing Basic auth this function can receive:

    'username:password' or a 'token'

    """
    user = User.verify_auth_token(username_or_token)
    if not user:
        user = User.query.filter_by(username=username_or_token).first()
        if not user or not user.verify_password(password):
            return False
    g.user = user
    return True
