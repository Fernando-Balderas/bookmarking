from flask import Blueprint, jsonify

routes_bp = Blueprint("routes", __name__)


@routes_bp.route("/", methods=["GET"])
def home():
    return jsonify({"msg": "Hello from REST API"})


@routes_bp.route("/posts", methods=["GET", "POST"])
def posts():
    return jsonify({"msg": "Accepted"})