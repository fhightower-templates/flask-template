clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log*

venv:
	virtualenv ~/.virtualenvs/{{cookiecutter.package_name}} && . ~/.virtualenvs/{{cookiecutter.package_name}}/bin/activate && pip3 install -r requirements.txt

run: venv
	python3 {{cookiecutter.package_name}}/{{cookiecutter.package_name}}.py

test: venv
	~/.virtualenvs/{{cookiecutter.package_name}}/bin/python3 -m unittest

sdist: venv test
	~/.virtualenvs/{{cookiecutter.package_name}}/bin/python3 setup.py sdist
