

default: test


clean_pyc:
	find . -name "*.pyc" -delete

clean_dist:
	rm -rf ./build
	rm -rf ./dist
	rm -rf ./*.egg-info

clean_reports:
	rm -rf ./public/*

clean_test_data:
	rm -rf ./tests/__pycache__
	rm -rf ./tests/.pytest_cache

clean_docker:
	docker-compose down

clean_all: clean_dist clean_pyc clean_docker clean_reports clean_test_data


build:
	python setup.py bdist_wheel


upload:
	twine upload -r elitsy ./dist/*.whl


bandit:
	docker-compose run django bandit -r ./attachments/ > reports/bandit.txt


test:
	$(MAKE) clean_pyc
	$(MAKE) clean_reports
	# Run `tox` on the image
	# docker run -t -v $(shell pwd):/app -v $(PIP_CACHE_DIR):/tmp/pip/ alekam/python-tox:latest tox
	docker-compose run django
	docker-compose stop


dockerbuild:
	# Build the docker image
	# Download Dockerfile from https://git.elitsy.ru/Docker/python-tox-builder/raw/master/Dockerfile?inline=false
	export PYPI_INDEX_URL=http://192.168.2.32:8081/repository/PyPI/simple PYPI_PRIVATE_URL=http://192.168.2.32:8081/repository/PrivatePyPI/ PYPI_PRIVATE_USER=admin PYPI_PRIVATE_PASSWORD=admin123 PYPI_PROXY_URL=http://192.168.2.32:8081/repository/PyPI/ PYPI_TRUSTED_HOST=192.168.2.32 && docker build -t git.elitsy.ru:5555/docker/python-tox-builder --build-arg PYPI_INDEX_URL --build-arg PYPI_TRUSTED_HOST --build-arg PIP_CACHE_DIR  --build-arg PYPI_PRIVATE_URL --build-arg PYPI_PRIVATE_USER --build-arg PYPI_PRIVATE_PASSWORD --build-arg PYPI_PROXY_URL .


#
# App repository format test
# you can use this command to copy template files to your forlder
# make check | xargs -I % cp ../django-app-template/% ./
#
LIST = .env .coveragerc .gitignore .gitlab-ci.yml MANIFEST.in Makefile docker-compose.yml run_tests.py tox.ini
LIST2 = README.rst setup.py tests
APP_TEMPLATE_PATH = ../django-app-template/
check:
	@for i in $(LIST); do \
		test -f $$i || echo $$i; \
	done
	@for i in $(LIST); do \
		$(MAKE) compare_files FILE=$$i; \
  done

compare_files:
	@FILE1=./$(FILE); \
	FILE2=$(APP_TEMPLATE_PATH)$(FILE); \
    if ! cmp -s $$FILE1 $$FILE2 ; then \
            echo "$(FILE)"; \
    fi

copy_missing_files:
	$(MAKE) check | xargs -I % cp $(APP_TEMPLATE_PATH)% ./

virtenv:
	virtualenv venv
	source ./venv/bin/activate; \
	pip install -r ./requirements.txt -r ./tests/requirements.txt \
		prospector "pylint<2.0.0" bandit flake8
