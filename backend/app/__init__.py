import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .config import app_config


def create_app(config_name):
    # create the Flask app
    app = Flask(__name__)
    # apply configs from config.py (debug settings)
    app.config.from_object(app_config[config_name])
    # set the database URL that we will connect to through SQLAlchemy (an object-relational mapper, AKA an ORM)
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://{username}:{password}@{host}:5432/{db}'.format(
        username=os.getenv('POSTGRES_USER'),
        password=os.getenv('POSTGRES_PASSWORD'),
        host=os.getenv('DB_HOST'),
        db=os.getenv('POSTGRES_DB')
    )
    # we don't use the Flask-SQLAlchemy event system so we turn this setting off (avoids console warnings)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # configure our data models and API routes
    # see the definition of models.init_app() in models/__init__.py
    # see the definition of routes.init_app() in routes/__init__.py
    from . import models, routes
    models.init_app(app)
    routes.init_app(app)

    return app
