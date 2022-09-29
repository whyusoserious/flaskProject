import json


def test_get_users(test_client):
    response = test_client.get('/users')
    assert response.status_code == 200


def test_create_user(test_client, create_user):
    response = test_client.post('/users', json=create_user)
    response_dict = json.loads(response.text)
    assert 'Quokaaa' == response_dict['name']
    assert len(response_dict) == 3
    assert response.status_code == 201


def test_update_user(test_client, update_user):
    response = test_client.put('/users/33', json=update_user)
    response_dict = json.loads(response.text)
    assert response_dict['email'] == 'changes@have.been.made'
    assert response.status_code == 200


def test_delete_user(test_client):
    response = test_client.delete('/users/33')
    assert response.status_code == 204


def test_delete_user_incorrect(test_client):
    response = test_client.delete('/users/104')
    assert response.status_code == 500
