from flask import Flask, jsonify
from flask_cors import CORS
from .config import Config
from app.database_connector import db


def create_app(config_override=None):
    app = Flask(__name__)
    app.config.from_object(Config)
    # if config_override:
    #     app.config.update(config_override)
    # db.init_app(app)
    # CORS(app, resources={r"/api/*": {"origins": app.config["FRONTEND_ORIGIN"]}})

    from . import models  # noqa: F401 - register ORM mappings
    from .api import register_blueprints
    register_blueprints(app)

    @app.errorhandler(404)
    def not_found(_):
        return jsonify(error="Not found"), 404

    return app
