SHELL := /bin/bash
# Fabric is not Python 3 compatible
python2 = $(shell which python2.7)
fab = $(shell which fab)

help:
	@echo "usage:"
	@echo "    make help             --  Show this help"
	@echo "    make deploy           --  Deploy on the server"
	@echo "    make install          --  Install NPM and Bower packages for the frontend"
	@echo "    make test             --  Run the tests"
	@echo "    make test-fast        --  Run the tests, and stop on failure"

install:
	pip install -r requirements.txt
	gem install sass
	gem install compass
	npm install
	grunt
	python manage.py migrate
	python manage.py runserver
    	
test:
	@coverage run manage.py test userprofile/tests
	@flake8 .
	@coverage report --fail-under=70

testfast:
	@python manage.py test --failfast

deploy:
	$(MAKE) install
	grunt dist
	$(python2) $(fab) deploy
