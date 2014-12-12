
all: setup_venv test

setup_venv: env/bin/activate env/.done

env/.done: setup.py
	env/bin/pip install -e .
	touch $@

env/bin/activate:
	virtualenv ./env

test: nose
	env/bin/nosetests . 

env/bin/nosetests:
	env/bin/pip install nose

nose: env/bin/nosetests
