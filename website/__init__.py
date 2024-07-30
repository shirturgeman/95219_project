from flask import Flask
from flask_sqlalchemy import SQLAlchemy


def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'hjshjhdjah kjshkjdhjs'
   
    from .app import app as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
