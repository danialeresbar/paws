#!/bin/sh

python manage.py migrate
python manage.py collectstatic --noinput
python manage.py loaddata development
python manage.py runserver 0.0.0.0:8080
