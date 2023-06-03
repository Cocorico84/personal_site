up:
	docker compose up --build

# run:
# 	python manage.py runserver

# migrate:
# 	python manage.py makemigrations
# 	python manage.py migrate

shell:
	docker compose run web python manage.py shell_plus

migrate:
	docker compose run web python3 manage.py makemigrations
	docker compose run web python3 manage.py migrate

user:
	docker compose run web python3 manage.py createsuperuser

format:
	pre-commit run --all-files

run:
	python manage.py runsslserver --certificate certs/cert.pem --key certs/key.pem

build:
	docker build . -t personal_site

push:
	docker push cocorico84/personal_site

.PHONY: up run migrate shell user format run build push
