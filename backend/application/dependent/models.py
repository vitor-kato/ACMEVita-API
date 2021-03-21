from .. import db
from ..base_model import BaseModel
from ..collaborator.models import Collaborator


class Dependent(BaseModel):
    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    full_name = db.Column(
        db.String,
        nullable=False,
    )
    collaborator_id = db.Column(
        db.Integer,
        db.ForeignKey(
            Collaborator.id,
            ondelete="CASCADE",
        ),
        nullable=True,
    )
    collaborator = db.relationship(
        "Collaborator",
        backref=db.backref(
            "dependents",
            lazy=True,
            passive_deletes=True,
        ),
        cascade="all,delete",
        passive_deletes=True,
    )
