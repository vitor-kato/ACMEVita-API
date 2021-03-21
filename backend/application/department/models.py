from .. import db
from ..base_model import BaseModel


class Department(BaseModel):
    id = db.Column(
        db.Integer,
        primary_key=True,
    )
    name = db.Column(
        db.String,
        unique=True,
        nullable=False,
        index=True,
    )

    def __repr__(self):
        return self.name
