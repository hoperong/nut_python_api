from app.user.models import User
from app.storage.db import get_session


def get_users():
    user = get_session().query(User).all()
    return user
