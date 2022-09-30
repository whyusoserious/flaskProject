import pytest
from app.__init__ import db


@pytest.fixture(scope="session")
def create_comm(test_client):
    db.session.begin_nested()
    new_comm = {
        "user": "Lube",
        "body": "Атass!"
    }

    yield new_comm


@pytest.fixture(scope="session")
def update_comm(test_client, create_comm):
    up_comm = create_comm
    up_comm['user'] = "okay@sorry.for.what"
    up_comm['body'] = "Oh sh*t, I'm sorry..."

    yield up_comm


@pytest.fixture(scope="session")
def delete_comm(test_client, create_comm):
    yield db.session.rollback()
