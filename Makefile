superuser:
	docker exec -it paws-application ./manage.py createsuperuser

bash:
	docker exec -it paws-application bash

shell:
	docker exec -it paws-application ./manage.py shell

makemigrations:
	docker exec -it paws-application ./manage.py makemigrations

migrate:
	docker exec -it paws-application ./manage.py migrate

test:
	docker exec -it paws-application ./manage.py test

statics:
	docker exec -it paws-application ./manage.py collectstatic --noinput

makemessages:
	docker exec -it paws-application django-admin makemessages

compilemessages:
	docker exec -it paws-application django-admin compilemessages
