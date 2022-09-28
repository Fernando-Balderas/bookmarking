import pytest
from app import create_app
from app.db import db


@pytest.fixture()
def app():
    app = create_app()
    app.config.update({
        "TESTING": True,
        "SQLALCHEMY_DATABASE_URI": "postgresql://testuser:testexamplepassword@localhost:5433/bookmarking_test",
        "SQLALCHEMY_TRACK_MODIFICATIONS": False
    })

    # other setup can go here
    with app.app_context():
        db.init_app(app)
        db.drop_all()
        db.create_all()

    yield app

    # clean up / reset resources here
    with app.app_context():
        db.session.remove()
        db.drop_all()


@pytest.fixture()
def client(app):
    return app.test_client()


@pytest.fixture()
def runner(app):
    return app.test_cli_runner()
