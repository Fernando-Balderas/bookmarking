from flask_sqlalchemy import SQLAlchemy


db = SQLAlchemy()


def create_db(app):
    with app.app_context():
        db.init_app(app)
        # db.drop_all()
        db.create_all()
        return db
