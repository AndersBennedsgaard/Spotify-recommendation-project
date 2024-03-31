.PHONY: install dev all lint test format clean

install:
	poetry install

dev:
	poetry install --with dev

all: lint format test

lint: dev
	poetry run pylint spotirecs/

test: dev
	poetry run pytest tests/ -v

format: dev
	poetry run black .
	poetry run isort .

clean:
	rm -f analysis/.cache
	rm -f analysis/track_features.csv
	rm -rf spotirecs/__pycache__
	rm -rf spotirecs.egg-info/
	rm -rf venv/
	rm -rf .pytest_cache/
