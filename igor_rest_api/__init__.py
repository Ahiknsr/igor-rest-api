from flask import Flask


def create_app():
    app = Flask(__name__)
    app.config.from_object('igor_rest_api.config')

    from igor_rest_api.api.routes import api
    api.init_app(app)

    from igor_rest_api.api.models import db
    db.init_app(app)

    # TODO: maybe add init_app() to flask-script
    from igor_rest_api.management import manager
    manager.app = app

    return app

app = create_app()
