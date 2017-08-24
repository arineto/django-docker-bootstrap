#!/bin/sh
python /app/manage.py collectstatic --noinput

gunicorn config.wsgi:application \
    --name=django-docker-bootstrap \
    --workers=4 \
    --worker-class=gevent \
    --bind=0.0.0.0:8000 \
    --chdir=/app \
    --timeout=120
