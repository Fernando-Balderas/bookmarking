from sqlalchemy import ForeignKey, func
from datetime import datetime
from .db import db


class Bookmark(db.Model):
    __tablename__ = "bookmarks"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    url = db.Column(db.String, nullable=False)
    folder_id = db.Column(db.Integer, ForeignKey("folders.id"), nullable=True)
    folder = db.relationship("Folder", back_populates="bookmarks")
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "folder_id": self.folder_id,
            "created_at": datetime.timestamp(self.created_at),
            "updated_at": datetime.timestamp(self.updated_at)
        }

    @property
    def serialize_populate(self):
        return {
            "id": self.id,
            "name": self.name,
            "url": self.url,
            "folder_id": self.folder_id,
            "folder": [f.serialize for f in self.folder],
            "created_at": datetime.timestamp(self.created_at),
            "updated_at": datetime.timestamp(self.updated_at)
        }


class Folder(db.Model):
    __tablename__ = "folders"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    bookmarks = db.relationship("Bookmark", back_populates="folder")
    created_at = db.Column(db.DateTime(timezone=True),
                           server_default=func.now())
    updated_at = db.Column(
        db.DateTime(timezone=True), server_default=func.now(), onupdate=func.now())

    @property
    def serialize(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "created_at": datetime.timestamp(self.created_at),
            "updated_at": datetime.timestamp(self.updated_at)
        }

    @property
    def serialize_populate(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "bookmarks": [b.serialize for b in self.bookmarks],
            "created_at": datetime.timestamp(self.created_at),
            "updated_at": datetime.timestamp(self.updated_at)
        }
