.PHONY: requirements.txt

dev:
	pip install --disable-pip-version-check -e .[dev]

install:
	pip install --disable-pip-version-check -r requirements.txt

requirements.txt: dev
	pipreqs --force

lint: dev
	pylint spotirecs/

test: dev
	python3 -m pytest tests/ -v

clean:
	rm -f analysis/.cache
	rm -f analysis/track_features.csv
	rm -rf spotirecs/__pycache__
	rm -rf venv/
