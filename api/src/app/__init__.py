import os
from flask import Flask
from flask_cors import CORS
from .models import *
from .routes.bookmarks import bookmarks_bp
from .routes.folders import folders_bp


def create_app(test_config=None):
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)

    if test_config is None:
        app.config.from_object('config')
        # app.config.from_pyfile("config.py", silent=True)
    else:
        app.config.from_mapping(test_config)
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    db.init_app(app)
    with app.app_context():
        # db.drop_all()
        db.create_all()

    app.register_blueprint(bookmarks_bp, url_prefix="/api/v1/bookmarks")
    app.register_blueprint(folders_bp, url_prefix="/api/v1/folders")

    return app
