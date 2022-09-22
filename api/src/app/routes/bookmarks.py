from flask import Blueprint, jsonify

bookmarks_bp = Blueprint("bookmarks", __name__)


@bookmarks_bp.route("", methods=["GET", "POST"])
def bookmarks():
    return jsonify({"data": []})


@bookmarks_bp.route("/folders/<folder_id>", methods=["GET"])
def bookmarksInFolder(folder_id):
    return jsonify({"data": []})


@bookmarks_bp.route("/<bookmark_id>", methods=["PUT", "DELETE"])
def bookmark(bookmark_id):
    return jsonify({"data": []})
