from flask import Blueprint

from app.config.common import config
from app.api_doc.controller import (
    get_api_doc_view,
    get_api_doc_html_view,
)

route = Blueprint('api_doc', __name__,
                  template_folder=config.get("API_DOC_TEMPLATES"))

route.add_url_rule('/v1/api_doc', view_func=get_api_doc_view, methods=["GET"])
route.add_url_rule('/v1/api_doc.html',
                   view_func=get_api_doc_html_view, methods=["GET"])
