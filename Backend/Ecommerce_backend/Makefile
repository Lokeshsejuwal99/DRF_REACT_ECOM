# Makefile

.PHONY: help install migrate runserver test

help:
	@echo "Available commands:"
	@echo "  make install    - Install project dependencies"
	@echo "  make migrate    - Apply database migrations"
	@echo "  make runserver  - Run the Django development server"
	@echo "  make test       - Run tests"

install:
	pip install -r requirements.txt

migration:
	python manage.py makemigrations
	python manage.py migrate
	python manage.py runserver

runserver:
	python manage.py runserver

test:
	python manage.py test
