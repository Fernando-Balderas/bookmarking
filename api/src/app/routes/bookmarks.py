from unicodedata import name
from flask import Blueprint, jsonify, request
from flask_api import status
from ..models import Bookmark, db

bookmarks_bp = Blueprint("bookmarks", __name__)


@bookmarks_bp.route("", methods=["GET", "POST"])
def bookmarks():
    if request.method == 'POST':
        body = request.get_json()
        print(body)
        bookmark = Bookmark(name=body.get('name'), url=body.get('url'))
        print(bookmark)
        db.session.add(bookmark)
        db.session.commit()
        return jsonify({
            "message": "Bookmark created",
            "data": bookmark.serialize
        }), status.HTTP_201_CREATED
    bookmarks = db.session.execute(db.select(Bookmark)).scalars().all()
    print(bookmarks)
    return jsonify({"data": [b.serialize for b in bookmarks]})


@bookmarks_bp.route("/folders/<folder_id>", methods=["GET"])
def bookmarksInFolder(folder_id):
    return jsonify({"data": []})


@bookmarks_bp.route("/<bookmark_id>", methods=["PUT", "DELETE"])
def bookmark(bookmark_id):
    return jsonify({"data": []})
