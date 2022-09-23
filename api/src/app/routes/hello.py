import json
from flask import Blueprint


hello_bp = Blueprint("hello", __name__)


@hello_bp.route("/hello", methods=["GET"])
def say_hello():
    return "Hello, World!"
