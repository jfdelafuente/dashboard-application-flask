import pytest
from app import db, create_app
from app.accounts.models import User
from config import TestingConfig


@pytest.fixture
def new_user():
    user = User(username='lolo',
                email='lolo@gmail.com',
                password='lolololo',
                is_admin=True)
    return user

@pytest.fixture
def test_client():
    flask_app = create_app(TestingConfig)
    with flask_app.app_context():
        with flask_app.test_client() as testing_client:
            yield testing_client


@pytest.fixture()
def init_database(test_client):
    
    # Create the database and the database table
    db.create_all()
    # Insert user data
    default_user = User(
        username="lolo", email="lolo@gmail.com", password="lolololo", is_admin=True
    )
    db.session.add(default_user)
    db.session.commit()

    yield  # this is where the testing happens!
    
    # Close the database session and drop all tables after the session
    db.session.remove()
    db.drop_all()


@pytest.fixture
def login_in_user(test_client):
    response = test_client.post(
            "/login",
            data=dict(username="lolo", password="lolololo"),
            follow_redirects=True,
    )
    yield
    test_client.get("/logout")