import pytest
from app.__init__ import db


@pytest.fixture(scope="session")
def create_post(test_client):
    db.session.begin_nested()
    new_post = {
        "title": "Family",
        "description": "Test is family deal."
    }

    yield new_post


@pytest.fixture(scope="session")
def update_post(test_client, create_post):
    up_post = create_post
    up_post['title'] = "changes@have.been.made"
    up_post['description'] = "Wish you were here T_T"

    yield up_post


@pytest.fixture(scope="session")
def delete_post(test_client, create_post):
    yield db.session.rollback()
