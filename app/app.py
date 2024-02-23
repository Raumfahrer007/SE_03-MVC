from flask import Flask
from app.blueprints import hello_world

def register_blueprints(app: Flask):
    app.register_blueprint(hello_world.controller.blueprint)

def create_app():
    app = Flask(__name__)
    app.config.from_object("app.config")

    register_blueprints(app)

    return app