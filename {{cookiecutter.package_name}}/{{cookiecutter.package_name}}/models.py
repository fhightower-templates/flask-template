#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from {{cookiecutter.package_name}} import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False)
    tags = db.Column(db.JSON)
