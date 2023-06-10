make check:
	poetry run flake8 gendiff
make install:
	python3 -m pip install --user dist/*.whl
make reinstall:
	python3 -m pip install --user --force-reinstall dist/*.whl
