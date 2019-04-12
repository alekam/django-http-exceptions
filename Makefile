

default: clean build upload


clean:
	rm -rf ./build
	rm -rf ./dist
	rm -rf ./*.egg-info

build:
	python setup.py bdist_wheel

upload:
	twine upload -r elitsy ./dist/*.whl
