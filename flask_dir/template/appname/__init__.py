from flask import Flask

def create_app():
    app = Flask(__name__)

    app.config.from_object('appname.settings')

    # register_extensions()
    # register_blueprints()

    return app

def register_extensions(app):
    pass 

def register_blueprints(app):
    pass 
