lint:
	poetry run flake8 gendiff
build: check
	poetry build
install:
	poetry install
reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl
test:
	poetry run pytest
selfcheck:
	poetry check

check: selfcheck test lint

test-coverage:
	poetry run pytest --cov=gendiff --cov-report xml

.PHONY: install selfcheck test lint check build
