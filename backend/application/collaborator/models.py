from .. import db
from ..base_model import BaseModel
from ..department.models import Department


class Collaborator(BaseModel):
    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    full_name = db.Column(
        db.String,
        nullable=False,
    )
    department_id = db.Column(
        db.Integer,
        db.ForeignKey(
            Department.id,
            ondelete="CASCADE",
        ),
        nullable=False,
    )
    department = db.relationship(
        "Department",
        backref=db.backref(
            "collaborators",
            lazy=True,
            passive_deletes=True,
        ),
        cascade="all,delete",
        passive_deletes=True,
    )

    @property
    def have_dependents(self):
        if self.dependents:
            return True
        return False
