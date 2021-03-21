import pytest
from sqlalchemy.exc import IntegrityError

from ...collaborator.models import Collaborator
from ...department.models import Department


def test_create_collaborator(client):
    department = Department(name="test")
    collaborator = Collaborator(full_name="test", department=department)
    collaborator.save()
    assert len(Collaborator.query.all()) == 1


def test_create_collaborator_with_no_department(client):
    with pytest.raises(IntegrityError):
        collaborator = Collaborator(full_name="test")
        collaborator.save()
