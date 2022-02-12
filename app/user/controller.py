from flask_babel import gettext
from flask import request
from werkzeug.security import generate_password_hash
from app.user.models import (
    User,
)
from app.user.dao import (
    get_user_list_by_page,
    get_user,
    get_user_by_account,
    create_user,
    update_user,
    delete_user,
    get_role_list_by_page,
    get_role,
    get_role_by_name,
    create_role,
    update_role,
    delete_role,
    update_role_function,
    get_module_list_by_page,
    get_module,
    get_function_list_by_page,
    get_function,
    get_permission_list_by_page,
    get_permission,
    get_resource_list_by_page,
    get_resource,
    get_action_list_by_page,
    get_action,
    get_user_role_list,
)

from app.core.exception import NotFoundException, ConflictException


def exists_user(account, id=None):
    """
    以account为主搜索
    如果id不为None，当user.id==id，则认为user不存在，这是为了更新设置的逻辑
    """
    user = get_user_by_account(account)
    if not user:
        return False, ""
    if id:
        if user.id == id:
            return False, ""
    return True, u"user account {} exists".format(account)


def exists_role(name, id=None):
    """
    以name为主搜索
    如果id不为None，当role.id==id，则认为role不存在，这是为了更新设置的逻辑
    """
    role = get_role_by_name(name)
    if not role:
        return False, ""
    if id:
        if role.id == id:
            return False, ""
    return True, u"role name {} exists".format(name)


def get_self_view():
    pass


def update_self_view():
    pass


def get_self_functions_view():
    pass


def get_self_menus_view():
    pass


def get_users_view():
    query = request.bind_query
    data, page_obj = get_user_list_by_page(query, query["page"], query["page_size"])
    for d in data:
        setattr(d, "role_list", [r.role for r in d.user_role_list])
    return {
        "page": page_obj["page"],
        "page_size": page_obj["page_size"],
        "total": page_obj["total"],
        "user_list": data,
    }


def create_user_view():
    body = request.bind_body
    result, msg = exists_user(body["account"])
    if result:
        raise ConflictException(gettext(msg))
    create_user(body)
    return


def get_user_view(user_id):
    user = get_user(user_id)
    if not user:
        raise NotFoundException(gettext(u"user {} not exists").format(user_id))
    setattr(user, "role_list", [r.role for r in user.user_role_list])
    return {"user": user}


def update_user_view(user_id):
    body = request.bind_body
    result, msg = exists_user(body["account"])
    if result:
        raise ConflictException(gettext(msg))
    update_user(user_id, body)
    return


def delete_user_view(user_id):
    user = get_user(user_id)
    if not user:
        raise NotFoundException(gettext(u"user {} not exists").format(user_id))
    delete_user(user_id)
    return


def get_roles_view():
    query = request.bind_query
    data, page_obj = get_role_list_by_page(query, query["page"], query["page_size"])
    return {
        "page": page_obj["page"],
        "page_size": page_obj["page_size"],
        "total": page_obj["total"],
        "role_list": data,
    }


def create_role_view():
    body = request.bind_body
    result, msg = exists_role(body["name"])
    if result:
        raise ConflictException(gettext(msg))
    create_role(body)
    return


def get_role_view(role_id):
    role = get_role(role_id)
    if not role:
        raise NotFoundException(gettext(u"role {} not exists").format(role_id))
    return {"role": role}


def update_role_view(role_id):
    body = request.bind_body
    result, msg = exists_role(body["name"])
    if result:
        raise ConflictException(gettext(msg))
    update_role(role_id, body)
    return


def delete_role_view(role_id):
    role = get_role(role_id)
    if not role:
        raise NotFoundException(gettext(u"role {} not exists").format(role_id))
    delete_role(role_id)
    return


def get_menus_view():
    pass


def get_role_menu_view(role_id):
    pass


def update_role_menu_view(role_id):
    pass


def get_functions_view():
    pass


def get_role_function_view(role_id):
    pass


def update_role_function_view(role_id):
    pass
