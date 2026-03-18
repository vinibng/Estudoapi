import pytest
from flask import Flask

from controladores.magic import cartinha_blueprint  


@pytest.fixture
def app():
    app = Flask(__name__)
    app.config["TESTING"] = True
    app.register_blueprint(cartinha_blueprint)
    return app


@pytest.fixture
def client(app):
    return app.test_client()