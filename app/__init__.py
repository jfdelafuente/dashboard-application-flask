from flask import Flask
from app.extensions import migrate, db, csrf, login_manager
from config import BaseConfig
from flask_cors import CORS

# ----------------------------------------------- #

def register_blueprints(app):
    from app.accounts.urls import accounts_bp
    from app.home.urls import home_bp
    # Registering blueprints
    app.register_blueprint(accounts_bp)
    app.register_blueprint(home_bp)
  

def initialize_plugins(app):
    # Initialize Plugins
    db.init_app(app)
    migrate.init_app(app, db)
    csrf.init_app(app)
    login_manager.init_app(app)
    CORS(app, resources={r"/*": {"origins": "*"}})


def create_app(app_config=BaseConfig):
    """Initialize the core application."""
    app = Flask(__name__)
    app.config.from_object(app_config)
    with app.app_context():
        initialize_plugins(app)
        register_blueprints(app)
    return app



# ----------------------------------------------- #

# Migrate Commands:
    # flask db init
    # flask db migrate
    # flask db upgrade
    # ERROR [flask_migrate] Error: Can't locate revision identified by 'ID' => flask db revision --rev-id ID