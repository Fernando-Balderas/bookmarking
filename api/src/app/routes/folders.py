from flask import Blueprint, jsonify

folders_bp = Blueprint("folders", __name__)


@folders_bp.route("/", methods=["GET", "POST"])
def folders():
    return jsonify({"data": []})

@folders_bp.route("/<folder_id>", methods=["PUT", "DELETE"])
def folder(folder_id):
    return jsonify({"data": []})