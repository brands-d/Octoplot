.PHONY: build

	install:
	pip install .

intall-dev:
	pip install -e .[dev]

intall-maintain:
	pip install -e .[dev,maintainer]

build:
	python setup.py sdist bdist_wheel

clean:
	python setup.py clean --all

publish:
	twine upload dist/*