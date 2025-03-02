from flask_login import UserMixin
from sqlalchemy import inspect
from datetime import datetime, timezone
from flask_validator import ValidateEmail, ValidateString, ValidateBoolean
from sqlalchemy.orm import validates

from app.extensions import db
from app.util import hash_pass

# ----------------------------------------------- #

# SQL Datatype Objects => https://docs.sqlalchemy.org/en/14/core/types.html
class User(db.Model, UserMixin):
    __tablename__ = "users"

    # Auto Generated Fields:
    id           = db.Column(db.Integer, primary_key=True)
    # created_on   = db.Column(db.DateTime(timezone.utc), default=datetime.now(timezone.utc))
    # updated_on   = db.Column(db.DateTime(timezone.utc), default=datetime.now(timezone.utc), onupdate=datetime.now(timezone.utc))
    created_on   = db.Column(db.DateTime(timezone=True), default=datetime.now)                           
    updated_on   = db.Column(db.DateTime(timezone=True), default=datetime.now, onupdate=datetime.now)
    
    # Input by User Fields:
    email        = db.Column(db.String(64), nullable=False, unique=True)
    username     = db.Column(db.String(64), nullable=False)
    # dob          = db.Column(db.Date)
    # country      = db.Column(db.String(100))
    # phone_number = db.Column(db.String(20))
    password     = db.Column(db.String, nullable=False)
    is_admin     = db.Column(db.Boolean, nullable=False, default=False)

    # Relations: SQLAlchemy Basic Relationship Patterns => https://docs.sqlalchemy.org/en/14/orm/basic_relationships.html
    # items = db.relationship("Item", back_populates='account')    # Account May Own Many Items => One to Many

    # Validations => https://flask-validator.readthedocs.io/en/latest/index.html
    @classmethod
    def __declare_last__(cls):
        ValidateEmail(User.email, True, True, "The email is not valid. Please check it") # True => Allow internationalized addresses, True => Check domain name resolution.
        ValidateString(User.username, True, True, "The username type must be string")
        # ValidateString(User.password, True, True, "The password type must be string")
        # ValidateBoolean(User.is_admin, True, True, "The is_admin type must be boolean")
        # ValidateCountry(Account.country, True, True, "The country is not valid")

    # Set an empty string to null for username field => https://stackoverflow.com/a/57294872
    @validates('username')
    def empty_string_to_null(self, key, value):
        if isinstance(value, str) and value == '': return None
        else: return value
    
    def __init__(self, **kwargs):
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, "__iter__") and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == "password":
                value = hash_pass(value)  # we need bytes here (not plain str)

            setattr(self, property, value)
    
    # How to serialize SqlAlchemy PostgreSQL Query to JSON => https://stackoverflow.com/a/46180522
    def toDict(self): 
        return { c.key: getattr(self, c.key) for c in inspect(self).mapper.column_attrs }

    def __repr__(self):
        return "<%r>" % self.email