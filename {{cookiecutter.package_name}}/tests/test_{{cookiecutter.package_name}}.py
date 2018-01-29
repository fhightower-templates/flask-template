#!/usr/bin/env python
# -*- coding: utf-8 -*-

import unittest

from {{cookiecutter.package_name}} import {{cookiecutter.package_name}}


class {{cookiecutter.package_name.replace('_', ' ').title().replace(' ', '')}}TestCase(unittest.TestCase):

    def setUp(self):
        self.app = {{cookiecutter.package_name}}.app.test_client()

    def test_get_index(self):
        rv = self.app.get('/')
        self.assertIn('{{cookiecutter.application_name}}', rv.data.decode())
        self.assertIn('{{cookiecutter.description}}', rv.data.decode())
        self.assertIn('Welcome!', rv.data.decode())
        self.assertIn('This is the start of something great.', rv.data.decode())
