import pytest
from app.__init__ import db


@pytest.fixture(scope="session")
def create_user(test_client):
    db.session.begin_nested()
    new_user = {
        "name": "Quokaaa",
        "email": "fast&furious@dominic.family"
    }

    yield new_user


@pytest.fixture(scope="session")
def update_user(test_client, create_user):
    up_user = create_user
    up_user['email'] = "changes@have.been.made"
    up_user['id'] = 112

    yield up_user


@pytest.fixture(scope="session")
def delete_user(test_client, create_user):
    yield db.session.rollback()