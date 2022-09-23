from flask import Blueprint, jsonify, request
from flask_api import status
from app.models import Folder, db

folders_bp = Blueprint("folders", __name__)


@folders_bp.route("", methods=["GET", "POST"])
def folders():
    if request.method == "POST":
        body = request.get_json()
        folder = Folder(name=body.get("name"))
        db.session.add(folder)
        db.session.commit()
        return jsonify({"message": "Folder created", "data": folder.serialize}), status.HTTP_201_CREATED
    folders = db.session.execute(db.select(Folder)).scalars().all()
    print(folders)
    return jsonify({"data": [f.serialize for f in folders]})


@folders_bp.route("/<folder_id>", methods=["PUT", "DELETE"])
def folder(folder_id):
    return jsonify({"data": []})
