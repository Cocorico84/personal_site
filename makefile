up:
	docker-compose up --build

run:
	python manage.py runserver

migrate:
	python manage.py makemigrations
	python manage.py migrate

.PHONY: up run