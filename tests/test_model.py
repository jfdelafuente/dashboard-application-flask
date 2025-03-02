from flask.testing import FlaskClient
from app import db
from app.accounts.models import User


def test_insert_valid_user(test_client: FlaskClient, init_database):
    user = User(email='john@example.com', username='john', password='johnjohn', is_admin=False)
    db.session.add(user)
    db.session.commit()
    john = User.query.filter(User.username.contains("john")).one()
    assert user.username == john.username
    assert user.email == john.email
    assert user.password == john.password

def test_new_user_with_fixture(new_user):
    """
    GIVEN a User model
    WHEN a new User is created
    THEN check the email and password fields are defined correctly
    """
    assert new_user.email == 'lolo@gmail.com'
    assert new_user.username == 'lolo'
    assert new_user.password != 'lolololo'
