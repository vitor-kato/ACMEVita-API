import pytest
from sqlalchemy.exc import IntegrityError

from ...department.models import Department


def test_create_department(client):
    department = Department(name="test")
    department.save()
    assert len(Department.query.all()) == 1


def test_no_duplicate(client):
    with pytest.raises(IntegrityError):
        for _ in range(3):
            department = Department(name="test")
            department.save()
