make lint:
	poetry run flake8 gendiff
build:
	poetry build
install:
	poetry install
reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl
test:
	poetry run pytest
check: test lint

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

.PHONY: install test lint check build
