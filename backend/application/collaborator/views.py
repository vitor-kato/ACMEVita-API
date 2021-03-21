from sqlalchemy.exc import IntegrityError

from .. import auth
from ..base_view import BaseView
from ..collaborator.models import Collaborator
from ..department.models import Department
from ..dependent.models import Dependent
from ..dependent.schemas import DependentsSchema
from .schemas import CollaboratorSchema


class CollaboratorView(BaseView):
    schema = CollaboratorSchema
    model = Collaborator

    @auth.login_required
    def get(self, id=None):
        if id:
            collaborator = self.model.query.filter_by(id=id).first_or_404(
                "Collaborator with id not found"
            )
            return self.jsonify(collaborator), 200

        return self.jsonify(self.model.query.all(), many=True), 200

    @auth.login_required
    def post(self):
        try:
            super(CollaboratorView, self).post()
            data = self.get_data()

            department = data.pop("department")
            department = Department.query.filter_by(name=department).first_or_404(
                "Department with name not found"
            )

            data["department"] = department
            collaborator = self.model(**data)
            collaborator.save()

            return self.jsonify(collaborator), 201
        except IntegrityError:
            self.abort(400, "Collaborator already exists")

    @auth.login_required
    def delete(self, id=None):
        collaborator = (
            self.model().query.filter_by(id=id).first_or_404("Collaborator not found")
        )
        collaborator.delete()
        return super(CollaboratorView, self).delete()

    @auth.login_required
    def put(self, id=None):
        try:
            super(CollaboratorView, self).put()
            collaborator = (
                self.model()
                .query.filter_by(id=id)
                .first_or_404("Collaborator not found")
            )
            data = self.get_data(partial=True)
            department = data.get("department")
            if department:
                department_instance = Department.query.filter_by(
                    name=department
                ).first_or_404("Department not found")
                collaborator.department = department_instance

            collaborator.full_name = data.get("full_name", collaborator.full_name)
            collaborator.save()
            return self.jsonify(collaborator), 200
        except IntegrityError:
            self.abort(400, "Collaborator already exists")


class CollaboratorDependents(BaseView):
    model = Dependent

    @auth.login_required
    def post(self, id=None):
        collaborator = Collaborator.query.filter_by(id=id).first_or_404(
            "Collaborator with id not found"
        )
        schema = DependentsSchema()
        data = self.get_data(schema)
        data["collaborator"] = collaborator
        dependent = self.model(**data)
        dependent.save()
        return schema.jsonify(dependent), 201
