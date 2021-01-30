clean:
	rm -rf venv && rm -rf *.egg-info && rm -rf dist && rm -rf *.log* && rm -fr .cache && rm -rf .pytest_cache

venv:
	virtualenv -p python3 ~/.virtualenvs/{{cookiecutter.package_name}} && . ~/.virtualenvs/{{cookiecutter.package_name}}/bin/activate && pip3 install -r requirements.txt

run:
	~/.virtualenvs/{{cookiecutter.package_name}}/bin/python {{cookiecutter.package_name}}/{{cookiecutter.package_name}}.py

test: clean
	~/.virtualenvs/{{cookiecutter.package_name}}/bin/python -m pytest

destroy:
	rm -rf ~/.virtualenvs/{{cookiecutter.package_name}}

init:
	. ~/.virtualenvs/{{cookiecutter.package_name}}/bin/activate && ~/.virtualenvs/{{cookiecutter.package_name}}/bin/python {{cookiecutter.package_name}}/manage.py db init

mg:
	~/.virtualenvs/{{cookiecutter.package_name}}/bin/python {{cookiecutter.package_name}}/manage.py db migrate

up:
	~/.virtualenvs/{{cookiecutter.package_name}}/bin/python {{cookiecutter.package_name}}/manage.py db upgrade
