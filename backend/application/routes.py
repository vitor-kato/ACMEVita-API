from typing import AnyStr

from application.collaborator.views import CollaboratorDependents, CollaboratorView
from application.department.views import DepartmentView
from application.user.views import UserView
from flask import current_app, g, jsonify

from . import auth


def register_api(
    view,
    endpoint: AnyStr,
    url: AnyStr,
    prefix="/api/",
    suffix="/",
    pk="id",
    pk_type="string",
):
    """Generates general mapping to all basic
    REST Verbs

    Args:
        view: ClassBased View
        endpoint: Endpoint name
        url: Url endpoint
        prefix (str, optional):  Defaults to "/api/".
        suffix (str, optional):  Defaults to "/".
        pk (str, optional):  Defaults to "id".
        pk_type (str, optional):  Defaults to "string".
    """
    view_func = view.as_view(endpoint)
    current_app.add_url_rule(
        prefix + url + suffix,
        defaults={pk: None},
        view_func=view_func,
        methods=[
            "GET",
        ],
    )
    current_app.add_url_rule(
        prefix + url + suffix,
        view_func=view_func,
        methods=[
            "POST",
        ],
    )
    current_app.add_url_rule(
        f"{prefix}{url}<{pk_type}:{pk}>{suffix}",
        view_func=view_func,
        methods=["GET", "PUT", "DELETE"],
    )


register_api(DepartmentView, endpoint="department", url="department/", pk="name")
register_api(UserView, endpoint="user", url="user/", pk="username")
register_api(
    CollaboratorView,
    endpoint="collaborator",
    url="collaborator/",
    pk="id",
    pk_type="int",
)

current_app.add_url_rule(
    "/api/collaborator/<int:id>/relationships/dependents/",
    view_func=CollaboratorDependents.as_view("add_collaborator"),
    methods=[
        "POST",
    ],
)


@current_app.route("/api/token/")
@auth.login_required
def get_auth_token():
    token = g.user.generate_auth_token()
    return jsonify({"token": token.decode("ascii")})
