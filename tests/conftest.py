import pytest

from app.__init__ import app
# from flask import jsonify, request
#
# from pytest_flask.fixtures import mimetype

class TestConf:
    def setup(self):
        app.testing = True
        self.client = app.test_client()

    def test_get_all_user(self):
        response = self.client.get('/users')
        assert response.status_code == 200

    def test_get_current_user(self):
        response = self.client.get('/users/2')
        assert response.status_code == 200

    def test_get_current_user_slash(self):
        response = self.client.get('/users/2/')
        assert response.status_code == 404

    def test_post_create_user(self):
        data = {
            'name' : 'Dominic',
            'email' : 'toretto@fast&furious.com',
            'forfakesake' : 'jesuscriste'
        }
        response = self.client.post('/users', json=data)
        assert response.status_code == 201

        assert len(response.get_json()) == 3

    def test_put_user(self):
        data = {
            'name': 'Joker',
            'email': 'DC@universe.com'
        }
        response = self.client.put('/users/9', json=data)
        assert response.status_code == 200

        assert len(response.get_json()) == 3

    def test_delete_user(self):
        response = self.client.delete('/users/9')
        assert response.status_code == 204

    def teardown(self):
        pass