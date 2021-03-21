# ACMEVita-API

## Built With

- [Flask](https://flask.palletsprojects.com/en/1.1.x/)
- [marshmallow](https://marshmallow.readthedocs.io/en/stable/)
- [Flask SQLAlchemy](https://flask-sqlalchemy.palletsprojects.com/en/2.x/)

## Getting Started

To get a local copy up and running follow these simple steps.

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [docker-compose](https://docs.docker.com/compose/install/)

### Installation

1. Clone the repo

   ```sh
   git clone https://github.com/vitor-kato/ACMEVita-API
   ```

2. Copy the .env.sample

   ```sh
   cp .env.sample .env
   ```

3. Use the convenience task runner to run the project.
   For more information click here [Taskfile](https://taskfile.dev)
   All the tasks are located at the Taskfile.yml

   ```sh
    ./task
   ```

## Usage

To use the API an authenticated user is required. This project is currently using Basic Auth for this purpose.
To create an user you can do the following with cURL:

```sh
curl --location --request POST 'http://127.0.0.1:5000/api/user/' \
--header 'Content-Type: application/json' \
--data-raw '{
    "username": "api",
    "password": "123"
}'

{
  "id": 1,
  "username": "api"
}


```

Now you can acess all protected view using the following:

```sh
curl --location --request GET 'http://127.0.0.1:5000/api/collaborator/' \
--header 'Authorization: Basic YXBpOjEyMw=='
```

Or using python requests:

```sh
import requests
from requests.auth import _basic_auth_str

url = "http://127.0.0.1:5000/api/collaborator/"

username = "api"
password = "123"
headers = {"Authorization": _basic_auth_str(username, password)}

response = requests.request("GET", url, headers=headers)

print(response.json())
```

### Postman

Postman documentation is also provided on the `docs/postman` directory
all endpoints are described in there with usage and examples

### Testing

Tests are done using pytest.

To run the tests use:

```sh
./task bash
pytest
```

### Roadmap

- Improve testing. Right now they are not DRY, they should be refactored using classes
- Improve Authentication. Basic auth is very limited and not secure. Its was done for illustration purposes
- Improve Users functions
- Improve the use of classes and their inheritance, to better handle repeated code and error validation

#### Additional Notes

This project was done in over a week. Where much of the Flask ecosystem is still a mystery
And much of the code was done with a lot of refactoring and trial and errors
But I learned a lot about Flask, flask app factory pattern and pytest (always used python unittest)
