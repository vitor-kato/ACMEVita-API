from flask import abort, current_app, json, jsonify, make_response
from flask.views import MethodView
from flask_restful import abort, request
from marshmallow import ValidationError
from werkzeug.exceptions import HTTPException


class BaseView(MethodView):
    """Generates reusable common methods for all views using
    flask MethodView

    Using this a default schema and model are available for the class
    """

    schema = None
    model = None

    def get_schema(self, many=False, exclude=[]):
        return self.schema(many=many, exclude=exclude)

    def get_data(self, schema=None, partial=False):
        schema = schema or self.get_schema()
        return schema.load(request.json, partial=partial)

    def jsonify(self, query, many=False, exclude=[]):
        return self.get_schema(many=many, exclude=exclude).jsonify(query)

    def get(self, *args, **kwargs):
        pass

    def post(self, *args, **kwargs):
        if not request.json:
            self.abort(400, "No data was received")

    def delete(self, *args, **kwargs):
        return jsonify({"success": True}), 204

    def put(self, *args, **kwargs):
        if not request.json:
            self.abort(400, "No data was received")

    def abort(self, status, reason="Invalid request"):
        abort(make_response(jsonify(errors=reason), status))


@current_app.errorhandler(HTTPException)
def handle_exception(e):
    """Return JSON instead of HTML for HTTP errors."""
    # start with the correct headers and status code from the error
    response = e.get_response()
    # replace the body with JSON
    response.data = json.dumps(
        {
            # "code": e.code,
            # "name": e.name,
            "error": e.description,
        }
    )
    response.content_type = "application/json"
    return response


@current_app.errorhandler(ValidationError)
def exception_handler(error):
    """Return JSON errors from Marshmallow validators"""
    return {"errors": error.messages}, 400
