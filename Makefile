.PHONY: build
.PHONY: test

	install:
	pip install .

install-dev:
	pip install -e .[dev]

install-maintain:
	pip install -e .[dev,maintainer]

build:
	python setup.py sdist bdist_wheel

clean:
	python setup.py clean --all

test:
	tox

publish:
	twine upload dist/*