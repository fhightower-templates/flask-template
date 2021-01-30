# Flask Template

[![Build Status](https://travis-ci.com/fhightower-templates/flask-template.svg?branch=master)](https://travis-ci.com/fhightower-templates/flask-template)

This is a simple [Flask](http://flask.pocoo.org) template that is ready for deployment to Heroku.

This template took inspiration from [https://github.com/datademofun/heroku-basic-flask](https://github.com/datademofun/heroku-basic-flask) and [https://github.com/candidtim/cookiecutter-flask-minimal](https://github.com/candidtim/cookiecutter-flask-minimal).

## Usage

```
cookiecutter https://github.com/fhightower-templates/flask-template.git
```

## Postgresql Setup

To setup postgresql:

```
psql

CREATE DATABASE <DATABASE_NAME>;
CREATE USER <DATABASE_USER> WITH PASSWORD '1234567';

ALTER ROLE <DATABASE_USER> SET client_encoding TO 'utf8';
ALTER ROLE <DATABASE_USER> SET default_transaction_isolation TO 'read committed';
ALTER ROLE <DATABASE_USER> SET timezone TO 'UTC';

GRANT ALL PRIVILEGES ON DATABASE <DATABASE_NAME> TO <DATABASE_USER>;
\q
```

After this is done, you will need to update config.py with the user name, password, and database name.
