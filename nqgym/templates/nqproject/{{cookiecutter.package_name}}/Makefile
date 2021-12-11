.PHONY: env install clean test codestyle coverage dist

PACKAGE_NAME={{cookiecutter.package_name}}

env:
	conda create -n ${PACKAGE_NAME} python={{cookiecutter.python_version}} -y

install:
	pip install -e .[dev]

clean:
	@rm -rf build
	@rm -rf dist
	@rm -rf .pytest_cache
	@find . -name '__pycache__' -exec rm -fr {} +
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~'    -exec rm -f {} +

test: clean
	pytest

codestyle: clean
	pycodestyle --statistics ${PACKAGE_NAME}

coverage: clean
	coverage erase
	coverage run -m pytest
	coverage report -m
	coverage html

dist: clean
	python setup.py sdist

release: clean dist
	twine upload dist/*
