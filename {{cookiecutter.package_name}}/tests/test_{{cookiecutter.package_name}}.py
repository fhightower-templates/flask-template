import unittest

from {{cookiecutter.package_name}} import {{cookiecutter.package_name}}


class {{cookiecutter.package_name.replace('_', ' ').title().replace(' ', '')}}TestCase(unittest.TestCase):

    def setUp(self):
        self.app = {{cookiecutter.package_name}}.app.test_client()

    def test_index(self):
        rv = self.app.get('/')
        self.assertIn('{{cookiecutter.application_name}}', rv.data.decode())
        self.assertIn('{{cookiecutter.description}}', rv.data.decode())


if __name__ == '__main__':
    unittest.main()
