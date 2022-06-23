import pytest
from flask import Flask


@pytest.fixture()
def app():
    app = Flask(__name__)
    app.secret_key = 'something_special'
    app.debug = True
    app.config.update({
        "TESTING": True,
    })
    yield app


@pytest.fixture()
def client(app):
    return app.test_client()
