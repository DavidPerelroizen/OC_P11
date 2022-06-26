import pytest
from flask import Flask


def create_app(config):
    app = Flask(__name__)
    app.config.from_object(config)
    return app


@pytest.fixture()
def client():
    app = create_app({"TESTING": True})
    yield app.test_client()
