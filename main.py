from flask import Flask
from routes import routes_bp


def init_app():
    app = Flask(__name__)
    app.register_blueprint(routes_bp)
    return app


if __name__ == '__main__':
    app = init_app()
    app.run(host='0.0.0.0')