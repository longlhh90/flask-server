import os
import dotenv
from flask import Flask
from apiconfig import api
from db import db


def create_app():
    dotenv.load_dotenv()
    flask_env = os.environ.get("FLASK_ENV", None)
    if flask_env == "development":
        configs = "settings.development"
    else:
        configs = "settings.production"

    # create and configure the app
    app = Flask(__name__)
    app.config.from_object(configs)
    api.init_app(app)
    db.init_app(app)

    @app.before_first_request
    def create_tables():
        db.create_all()
    return app


if __name__ == "__main__":
    app = create_app()
