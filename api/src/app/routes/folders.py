from flask import Blueprint, jsonify, request
from flask_api import status
from sqlalchemy import exc
from app.models import Folder, db

folders_bp = Blueprint("folders", __name__)


@folders_bp.route("", methods=["GET", "POST"])
def folders():
    try:
        if request.method == "POST":
            body = request.get_json()
            folder = Folder(name=body.get("name"),
                            description=body.get("description"))
            db.session.add(folder)
            db.session.commit()
            return jsonify({"message": "Folder created", "data": folder.serialize}), status.HTTP_201_CREATED
        folders = db.session.execute(db.select(Folder)).scalars().all()
        # TODO: Add not found response
        return jsonify({"data": [f.serialize for f in folders]})
    except exc.SQLAlchemyError as e:
        return jsonify({"message": "Error"}), 400


@folders_bp.route("/<folder_id>", methods=["PUT", "DELETE"])
def folder(folder_id):
    try:
        folder = db.session.execute(
            db.select(Folder).where(Folder.id == folder_id)).scalars().one()
        if request.method == "PUT":
            body = request.get_json()
            folder.name = body.get("name")
            folder.description = body.get("description")
            db.session.commit()
            message = "Folder updated"
        elif request.method == "DELETE":
            db.session.delete(folder)
            db.session.commit()
            message = "Folder deleted"
        return jsonify({"message": message, "data": folder_id})
    except exc.SQLAlchemyError as e:
        if isinstance(e, exc.NoResultFound):
            return jsonify({"message": "Bookmark not found"}), status.HTTP_404_NOT_FOUND
        return jsonify({"message": "Error"}), status.HTTP_500_INTERNAL_SERVER_ERROR
