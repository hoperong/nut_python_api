from flask import Blueprint

route = Blueprint('simple_page', __name__,
                        template_folder='templates')

@route.route('/', defaults={'page': 'index'})
@route.route('/<page>')
def show(page):
    return "Holle World!"