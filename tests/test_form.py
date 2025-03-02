from flask.testing import FlaskClient
from app.accounts.forms import RegisterForm, LoginForm

def test_validate_success_register_form(test_client: FlaskClient, init_database: None):
    """Ensure correct data validates."""
    form = RegisterForm(username="new_user",
                        email="new_user@gmail.com",
                        password="useruseruser",
                        confirm_password="useruseruser")
    assert form.validate() is True

def test_validate_fail_username_register_form(test_client: FlaskClient):
    """Ensure incorrect data does not validate."""
    form = RegisterForm(username="new",
                        email="lolo@gmail.com",
                        password="lolo",
                        confirm_password="lolo")
    assert form.validate() is False
    assert "Field must be between 4 and 25 characters long." in form.username.errors
    

def test_validate_fail_email_register_form(test_client: FlaskClient):
    """Ensure user can't register when a duplicate username is used."""
    form = RegisterForm(username="lolo",
                        email="lolo",
                        password="lolo",
                        confirm_password="lolo")
    assert form.validate() is False
    assert "Invalid email address." in form.email.errors
    
def test_validate_fail_password_register_form(test_client: FlaskClient):
    """Ensure user can't register when a duplicate email is used."""
    form = RegisterForm(username="lolo",
                        email="lolo@gmail.com",
                        password="lolo",
                        confirm_password="lolo")
    assert form.validate() is False
    assert "Field must be at least 8 characters long." in form.password.errors
    
def test_validate_fail_confirm_password_register_form(test_client: FlaskClient):
    """Ensure user can't register when a duplicate email is used."""
    form = RegisterForm(username="lolo",
                        email="lolololo",
                        password="lololola",
                        confirm_password="lolo")
    assert form.validate() is False
    assert "Passwords must match." in form.confirm_password.errors


def test_validate_success_login_form(test_client: FlaskClient):
    """Ensure correct data validates."""
    form = LoginForm(username="new_user", password="newnewnew")
    assert form.validate() is True

# No hay validaciones de los campos de login y password en el formulario de login
# Desarrolo por hacer. Aunque es mejor no incluir validaciones en el formulario de login
# ya que no se necesita validar si el usuario y contraseña son correctos
def test_validate_success_login_form(test_client: FlaskClient):
    """Ensure incorrect data does not validate."""
    form = LoginForm(username="neww", password="newnewnew")
    assert form.validate() is True

# def test_validate_fail_username_login_form(test_client: FlaskClient):
#     """Ensure incorrect data does not validate."""
#     form = LoginForm(username="new", password="newnewnew")
#     assert form.validate() is False
#     assert "Field must be at least 4 characters long." in form.username.errors
    
# def test_validate_fail_password_login_form(test_client: FlaskClient):
#     """Ensure incorrect data does not validate."""
#     form = LoginForm(username="new_user", password="new")
#     assert form.validate() is False
#     assert "Field must be at least 8 characters long." in form.password.errors