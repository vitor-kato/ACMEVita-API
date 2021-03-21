import pytest
from requests.auth import _basic_auth_str

from .. import db, init_app
from ..user.models import User

app = init_app()
app.app_context().push()


username = "test"
password = "test"
AUTH_HEADER = {"Authorization": _basic_auth_str(username, password)}


@pytest.fixture(scope="session", autouse=True)
def set_db():
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:////test.db"
    app.config["TESTING"] = True


@pytest.fixture(autouse=True)
def client(set_db):
    with app.test_client() as client:
        with app.app_context():
            db.drop_all()
            db.create_all()
            create_user()

        yield client


def create_user():
    user = User(username=username)
    user.hash_password(password)
    user.save()
