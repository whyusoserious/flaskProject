import pytest
from flask import *
from app.__init__ import app, db
from app.migrations import User


@pytest.fixture(scope="session")
def test_client():
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


@pytest.fixture(scope="session")
def create_user(test_client):
    newUser = {
        "name":"Quokaaa",
        "email":"fast&furious@dominic.family"
    }

    yield newUser


@pytest.fixture(scope="session")
def update_user(test_client, create_user):
    updateUser = create_user
    updateUser['email'] = "changes@have.been.made"
    updateUser['id'] = 33

    yield updateUser