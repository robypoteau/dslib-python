all:
	$(error please pick a target)

env:
	# Create venv directory if not exist
	test -d env || virtualenv env
	./env/bin/python -m pip install -r requirements.txt

dev-env: env
	./env/bin/python -m pip install -r requirements-dev.txt

test:
	find . -name '*.pyc' -exec rm -f {} \;
	./env/bin/flake8 dslib tests
	./env/bin/python -m pytest \
	    --doctest-modules \
	    --disable-warnings \
	    --verbose \
	    dslib tests

build-doc:
	cd docsrc && make html
	cp -a docsrc/build/html/ docs

package:
	python setup.py sdist

clean:
	rm -rf build dist nlp.egg-info
