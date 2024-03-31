.PHONY: install dev all lint test format clean

install:
	poetry install

dev:
	poetry install --with dev

all: lint format test

lint: dev
	poetry run ruff check .

format: dev
	poetry run ruff format .

# test: dev
# 	poetry run pytest tests/ -v

clean:
	rm -f analysis/.cache
	rm -f analysis/track_features.csv
	rm -rf spotirecs.egg-info/
	rm -rf .pytest_cache/
	rm -rf .ruff_cache/
	find . -type d -name __pycache__ -exec rm -r {} \+
