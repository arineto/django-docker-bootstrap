#!/bin/bash

set -e

if [ $1 = "/gunicorn.sh" ] || [ $3 = "runserver" ]; then
    python /app/manage.py migrate
fi

exec "$@"
