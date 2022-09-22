from flask_sqlalchemy import SQLAlchemy
# from sqlalchemy.sql import func
from sqlalchemy import ForeignKey, func

db = SQLAlchemy()


class Bookmark(db.Model):
    __tablename__ = "bookmarks"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    folderId = db.Column(db.Integer, ForeignKey("folders.id"), nullable=True)
    folder = db.relationship("Folder", back_populates="bookmarks")
    createdAt = db.Column(db.DateTime(), server_default=func.now())
    updatedAt = db.Column(
        db.DateTime(), server_default=func.now(), onupdate=func.current_timestamp())

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
        }


class Folder(db.Model):
    __tablename__ = "folders"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    bookmarks = db.relationship("Bookmark", back_populates="folder")
    createdAt = db.Column(db.DateTime(), server_default=func.now())
    updatedAt = db.Column(
        db.DateTime(), server_default=func.now(), onupdate=func.current_timestamp())

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
        }
