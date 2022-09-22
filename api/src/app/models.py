from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Bookmarking(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
