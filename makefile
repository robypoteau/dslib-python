.PHONY: help
help:
	@echo "Usage:"
	@grep -E '^[a-zA-Z_-]+:.*?## .*$$' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[36m  %-15s\033[0m %s\n", $$1, $$2}'

env: ## Create an virtualenv environment
	# Create env directory if not exist
	test -d env || virtualenv env
	./env/bin/python -m pip install -r requirements.txt

dev-env: env ## Create an virtualenv dev environment
	./env/bin/python -m pip install -r requirements.txt

test:  ## Run the test suite and linter
	find . -name '*.pyc' -exec rm -f {} \;
	./env/bin/flake8 dslib tests
	./env/bin/python -m pytest \
	    --doctest-modules \
	    --disable-warnings \
	    --verbose \
	    dslib tests

test_%: ##Run the test for an individual file (for personal use)
	find . -name '*.pyc' -exec rm -f {} \;
	./env/bin/flake8 dslib/$*.py tests/$@.py
	./env/bin/python -m pytest \
			--doctest-modules \
			--disable-warnings \
			--verbose \
			dslib/$*.py tests/$@.py

build-doc: ## Build the Sphinx documentation
	cd docsrc && make html
	cp -a docsrc/build/html/ docs

package: ## Package the library
	python setup.py sdist

clean: ## Clean the build and dist folder
	rm -rf build dist nlp.egg-info
