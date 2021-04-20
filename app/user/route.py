from app.user.controller import (
    get_users_view,
    create_user_view,
    get_user_view,
    update_user_view,
    delete_user_view,
)

from app.user.schema import (
    GetUsersInSc,
    GetUsersOutSc,
)

from flask import Blueprint

from app.core.app import ViewFuncWrapper

route = Blueprint('user', __name__)

route.add_url_rule(
    '/v1/users', view_func=ViewFuncWrapper(get_users_view, query=GetUsersInSc, responses={
        "200": {"schema": GetUsersOutSc, "description": "获取用户列表"}
    }, tags=["user"]), methods=["GET"])
route.add_url_rule('/v1/users', view_func=create_user_view, methods=["POST"])
route.add_url_rule('/v1/users/<int:user_id>', view_func=ViewFuncWrapper(get_user_view, query=GetUsersInSc, responses={
    "200": {"schema": GetUsersOutSc, "description": "获取用户列表"}
}, tags=["user"]), methods=["GET"])
route.add_url_rule('/v1/users/<user_id>',
                   view_func=update_user_view, methods=["PUT"])
route.add_url_rule('/v1/users/<user_id>',
                   view_func=delete_user_view, methods=["DELETE"])
