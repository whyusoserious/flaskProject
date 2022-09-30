import pytest
from flask import *
from app.__init__ import app, db


@pytest.fixture(scope="session")
def test_client():
    with app.test_client() as testing_client:
        with app.app_context():
            yield testing_client


# @pytest.yield_fixture(scope="session", autouse=True)
# def session_db():
#     db.session.begin_nested()
#     yield  # db.session
#     db.session.rollback()
