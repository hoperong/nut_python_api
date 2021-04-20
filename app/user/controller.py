from app.user.dao import (
    get_users
)

from flask_babel import gettext


def get_users_view():
    return get_users()


def create_user_view():
    pass


def get_user_view(user_id):
    return str(gettext(u'hello world'))


def update_user_view(user_id):
    pass


def delete_user_view(user_id):
    pass
