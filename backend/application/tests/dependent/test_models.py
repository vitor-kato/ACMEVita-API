from ...collaborator.models import Collaborator
from ...department.models import Department
from ...dependent.models import Dependent


def test_create_dependent(client):
    department = Department(name="test")
    department.save()
    collaborator = Collaborator(full_name="test", department=department)
    collaborator.save()
    dependent = Dependent(full_name="test", collaborator=collaborator)
    dependent.save()
    assert len(dependent.query.all()) == 1
