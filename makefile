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

.PHONY: up run migrate shell user format
