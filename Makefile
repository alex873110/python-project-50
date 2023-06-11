make check:
	poetry run flake8 gendiff
build:
	poetry build
install:
	poetry install
reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl
