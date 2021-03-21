from sqlalchemy.exc import IntegrityError

from .. import auth
from ..base_view import BaseView
from .models import Department
from .schemas import DepartmentSchema


class DepartmentView(BaseView):
    schema = DepartmentSchema
    model = Department

    @auth.login_required
    def get(self, name=None):
        if name:
            department = self.model.query.filter_by(name=name).first_or_404(
                "Department with name not found"
            )
            return self.jsonify(department)

        return self.jsonify(
            self.model.query.all(), many=True, exclude=["collaborators"]
        )

    @auth.login_required
    def post(self):
        try:
            data = self.get_data()
            department = self.model(**data)
            department.save()
            return self.jsonify(department), 201
        except IntegrityError:
            self.abort(400, "Department already exists")

    @auth.login_required
    def delete(self, name=None):
        department = (
            self.model().query.filter_by(name=name).first_or_404("Department not found")
        )
        department.delete()
        return super(DepartmentView, self).delete()

    @auth.login_required
    def put(self, name=None):
        try:
            super(DepartmentView, self).put()
            department = (
                self.model()
                .query.filter_by(name=name)
                .first_or_404("Department not found")
            )
            data = self.get_data()

            department.name = data.get("name", department.name)
            department.save()
            return self.jsonify(department), 200
        except IntegrityError:
            self.abort(400, "Department with this name already exists")
