from ...collaborator.models import Collaborator
from ...department.models import Department
from ..conftest import AUTH_HEADER


def test_get_department_list(client):
    c = client.get("/api/collaborator/", headers=AUTH_HEADER)
    assert c.status_code == 200


def test_get_non_existent_collaborator(client):
    c = client.get("/api/collaborator/foobar/", headers=AUTH_HEADER)
    assert c.status_code == 404


def test_get_existent_collaborator(client):
    department = Department(name="test")
    department.save()
    collaborator = Collaborator(full_name="test", department=department)
    collaborator.save()
    c = client.get(f"/api/collaborator/{collaborator.id}/", headers=AUTH_HEADER)

    resp = c.get_json()
    assert c.status_code == 200
    assert resp["full_name"] == "test"
    assert resp["department"] == "test"


def test_create_create_collaborator(client):
    department = Department(name="test")
    department.save()
    data = {"full_name": "test", "department": department.name}
    c = client.post("/api/collaborator/", headers=AUTH_HEADER, json=data)
    assert c.status_code == 201


def test_add_dependent_to_collaborator(client):
    department = Department(name="test")
    department.save()
    collaborator = Collaborator(full_name="test", department=department)
    collaborator.save()

    data = {"full_name": "test"}
    c = client.post(
        f"api/collaborator/{collaborator.id}/relationships/dependents/",
        headers=AUTH_HEADER,
        json=data,
    )
    assert c.status_code == 201


def test_bad_request(client):
    data = {"non_existent_field": "test"}
    c = client.post("/api/collaborator/", headers=AUTH_HEADER, json=data)
    assert c.status_code == 400
