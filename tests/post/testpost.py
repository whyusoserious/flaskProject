import json
from tests.post.confpost import create_post, update_post, delete_post


def test_get_posts(test_client):
    response = test_client.get('/users/1/posts')
    assert response.status_code == 200


def test_create_post(test_client, create_post):
    response = test_client.post('/users/1/posts', json=create_post)
    response_dict = json.loads(response.text)
    assert 'Test is family deal.' == response_dict['description']
    assert len(response_dict) == 4
    assert response.status_code == 201


def test_update_post(test_client, update_post):
    response = test_client.put('/users/1/posts/2', json=update_post)
    response_dict = json.loads(response.text)
    assert 'Wish you were here T_T' == response_dict['description']
    assert response.status_code == 200


def test_delete_post(test_client, delete_post):
    response = test_client.delete('/users/1/posts/2')
    assert response.status_code == 204


def test_delete_post_incorrect(test_client):
    response = test_client.delete('/users/1/posts/0')
    assert response.status_code == 500
