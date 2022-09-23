from flask import Blueprint, jsonify, request
from flask_api import status
from sqlalchemy import exc
from app.models import Bookmark, db

bookmarks_bp = Blueprint("bookmarks", __name__)


@bookmarks_bp.route("", methods=["GET", "POST"])
def bookmarks():
    if request.method == "POST":
        body = request.get_json()
        bookmark = Bookmark(name=body.get("name"), url=body.get(
            "url"), folder_id=body.get("folderId"))
        db.session.add(bookmark)
        db.session.commit()
        return jsonify({
            "message": "Bookmark created",
            "data": bookmark.serialize
        }), status.HTTP_201_CREATED
    bookmarks = db.session.execute(db.select(Bookmark)).scalars().all()
    # TODO: Add not found response
    return jsonify({"data": [b.serialize for b in bookmarks]})


@bookmarks_bp.route("/folders/<folder_id>", methods=["GET"])
def bookmarks_in_folder(folder_id):
    bookmarks = db.session.execute(
        db.select(Bookmark).where(Bookmark.folder_id == folder_id)).scalars().all()
    # TODO: Add not found response
    return jsonify({"data": [b.serialize for b in bookmarks]})


@bookmarks_bp.route("/<bookmark_id>", methods=["PUT", "DELETE"])
def bookmark(bookmark_id):
    try:
        bookmark = db.session.execute(
            db.select(Bookmark).where(Bookmark.id == bookmark_id)).scalars().one()
        if request.method == "PUT":
            body = request.get_json()
            bookmark.name = body.get("name")
            bookmark.url = body.get("url")
            bookmark.folder_id = body.get("folderId")
            db.session.commit()
            message = "Bookmark updated"
        elif request.method == "DELETE":
            db.session.delete(bookmark)
            db.session.commit()
            message = "Bookmark deleted"
        return jsonify({"message": message, "data": bookmark_id})
    except exc.SQLAlchemyError as e:
        if isinstance(e, exc.NoResultFound):
            return jsonify({"message": "Bookmark not found"}), status.HTTP_404_NOT_FOUND
        elif isinstance(e, exc.IntegrityError):
            return jsonify({"message": "Invalid parameters"}), status.HTTP_400_BAD_REQUEST
        return jsonify({"message": "Error"}), status.HTTP_500_INTERNAL_SERVER_ERROR
