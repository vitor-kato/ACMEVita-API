from ...department.models import Department
from ..conftest import AUTH_HEADER


def test_get_department_list(client):
    c = client.get("/api/department/", headers=AUTH_HEADER)
    assert c.status_code == 200


def test_get_non_existent_department(client):
    c = client.get("/api/department/foobar/", headers=AUTH_HEADER)
    assert c.status_code == 404


def test_get_existent_department(client):
    name = "test"
    department = Department(name=name)
    department.save()
    c = client.get(f"/api/department/{name}/", headers=AUTH_HEADER)

    resp = c.get_json()
    assert c.status_code == 200
    assert resp["collaborators"] == []
    assert resp["name"] == name


def test_create_department(client):
    data = {"name": "test"}
    c = client.post("/api/department/", headers=AUTH_HEADER, json=data)
    assert c.status_code == 201


def test_bad_request(client):
    data = {"non_existent_field": ""}
    c = client.post("/api/department/", headers=AUTH_HEADER, json=data)
    assert c.status_code == 400
