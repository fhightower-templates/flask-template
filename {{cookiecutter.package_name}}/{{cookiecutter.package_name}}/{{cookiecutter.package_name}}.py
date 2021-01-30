#!/usr/bin/env python
# -*- coding: utf-8 -*-

{% if cookiecutter.use_postgresql == 'y' %}
import random

from flask import flash, Flask, render_template, redirect, request, url_for
from flask_sqlalchemy import SQLAlchemy
{% else %}
from flask import flash, Flask, render_template, redirect, request, url_for
{% endif %}

app = Flask(__name__)
app.secret_key = 'abc'
{%- if cookiecutter.use_postgresql == 'y' %}
app.config.from_pyfile('config.py')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

try:
    from models import User
except ImportError:
    pass


@app.route("/")
def index():
    # request.form['text']
    # request.args.get('text')
    return render_template('index.html', users=User.query.all())


@app.route("/users/<user_id>")
def details(user_id):
    user = db.session.query(User).filter(User.id == user_id).first()
    print('user {}'.format(user))
    return render_template('details.html', user=user)


@app.route('/search')
def search():
    query = request.args.get('q')

    if query:
        results = db.session.query(User).filter(User.name.ilike('%{}%'.format(query))).all()
        print('results {}'.format(results))
        return render_template('search.html', results=results)
    else:
        return render_template('search.html')


@app.route('/new')
def new():
    name = request.args.get('name')
    new_user = User(name=name, tags=[name[::-1], 'foo', random.randint(0, 10)])
    db.session.add(new_user)
    db.session.commit()
    return redirect('/', code=302)


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
{% else %}


@app.route("/")
def index():
    # request.form['text']
    # request.args.get('text')
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True, use_reloader=True)
{% endif %}
