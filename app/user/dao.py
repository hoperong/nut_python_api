from flask_babel import gettext
from app.storage.db import get_session

from app.user.models import (
    User,
    Role,
    UserRole,
    Function,
    Permission,
)

from app.core.exception import InternalServerError


def get_user_list_by_page(query, page=1, page_size=10):
    query = (
        get_session()
        .query(User)
        .filter(
            User.account.like("%{}%".format(query["q"]))
            | User.name.like("%{}%".format(query["q"]))
        )
    )
    total = query.count()
    result = query.paginate(page, page_size).all()
    return result, {"page": page, "page_size": page_size, "total": total}


def get_user(id):
    user = get_session().query(User).filter(User.id == id).first()
    return user


def get_user_by_account(account):
    user = get_session().query(User).filter(User.account == account).first()
    return user


def create_user(data):
    user = User(
        account=data.get("account", ""),
        password=data.get("password", ""),
        name=data.get("name", ""),
    )
    get_session().add(user)
    user_role_list = []
    for role_id in data["role_id_list"]:
        role = get_session().query(Role).filter(Role.id == role_id).first()
        if not role:
            continue
        user_role = UserRole(user_id=user.id, role_id=role_id)
        user_role_list.append(user_role)
    get_session().bulk_save_objects(user_role_list)
    get_session().flush()
    return


def update_user(id, data):
    user = get_session().query(User).filter(User.id == id).first()
    if not user:
        return
    user.save()
    get_session().flush()
    return


def delete_user(id):
    user = get_session().query(User).filter(User.id == id).first()
    user.is_frozen = True
    user.save()
    get_session().flush()
    return


def get_user_role_list(user_id):
    result = get_session().query(UserRole).filter(UserRole.user_id == user_id).all()
    return result


def get_role_list_by_page(query, page=1, page_size=10):
    query = get_session().query(Role).filter(User.name.like("%{}%".format(query["q"])))
    total = query.count()
    result = query.paginate(page, page_size).all()
    return result, {"page": page, "page_size": page_size, "total": total}


def get_role(id):
    role = get_session().query(Role).filter(Role.id == id).first()
    return role


def get_role_by_name(name):
    role = get_session().query(Role).filter(Role.name == name).first()
    return role


def create_role(data):
    role = Role(
        name=data.get("name", ""),
    )
    get_session().add(role)
    get_session().flush()
    return


def update_role(id, data):
    role = get_session().query(Role).filter(Role.id == id).first()
    if not role:
        return
    role.save()
    get_session().flush()
    return


def delete_role(id):
    user_role_count = (
        get_session().query(UserRole).filter(UserRole.role_id == id).count()
    )
    if user_role_count > 0:
        raise InternalServerError(gettext(u"role don`t delete by using"))
    role = get_session().query(Role).filter(Role.id == id).first()
    get_session().delete(role)
    get_session().flush()
    return