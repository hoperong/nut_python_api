from flask import Blueprint

from app.index.controller import(
    ping
)

route = Blueprint('index', __name__)

route.add_url_rule('/ping', view_func=ping, methods=["GET"])
