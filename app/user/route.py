from flask import Blueprint
from flask_babel import lazy_gettext as gettext

route = Blueprint('simple_page', __name__)


@route.route('/', defaults={'page': 'index'})
@route.route('/<page>')
def show(page):
    return gettext("Hello World!")
