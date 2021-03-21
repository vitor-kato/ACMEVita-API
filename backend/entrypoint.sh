#!/bin/sh

./wait-for-it.sh $DB_HOST:$DB_PORT

export FLASK_APP=wsgi.py

flask create-all
python wsgi.py

exec "$@"
