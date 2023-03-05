.PHONY: requirements.txt

dev:
	pip install --user --disable-pip-version-check -e .[dev]

install:
	pip install --user --disable-pip-version-check -r requirements.txt

requirements.txt:
	pipreqs --force

lint:
	pylint spotirecs/

test:
	python3 -m pytest tests/ -v

clean:
	rm analysis/.cache
	rm analysis/track_features.csv
	rm -rf spotirecs/__pycache__
