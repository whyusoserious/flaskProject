import json
from tests.comment.confcomm import create_comm, update_comm, delete_comm


def test_get_comments(test_client):
    response = test_client.get('/users/1/posts/1/comments')
    assert response.status_code == 200


def test_create_comment(test_client, create_comm):
    response = test_client.post('/users/1/posts/1/comments', json=create_comm)
    response_dict = json.loads(response.text)
    assert 'Атass!' == response_dict['body']
    assert len(response_dict) == 5
    assert response.status_code == 201


def test_update_comment(test_client, update_comm):
    response = test_client.put('/users/1/posts/1/comments/2', json=update_comm)
    response_dict = json.loads(response.text)
    assert "Oh sh*t, I'm sorry..." == response_dict['body']
    assert response.status_code == 200


def test_delete_comment(test_client, delete_comm):
    response = test_client.delete('/users/1/posts/1/comments/2')
    assert response.status_code == 204


def test_delete_comment_incorrect(test_client):
    response = test_client.delete('/users/1/posts/1/comments/777')
    assert response.status_code == 500
