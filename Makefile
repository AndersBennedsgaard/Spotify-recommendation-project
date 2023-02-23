.PHONY: requirements.txt

dev:
	mkdir -p tmp
	pip install --disable-pip-version-check -e .[dev]

install:
	pip install --disable-pip-version-check -r requirements.txt

requirements.txt: install
	pipreqs --force

lint:
	pylint src/ # --rcfile=.github/pylintrc.ini
	# pylint tests/ # --rcfile=.github/pylintrc.ini

test:
	python3 -m pytest tests/ -v

clean:
	rm -rf tmp/