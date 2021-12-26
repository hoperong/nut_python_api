from flask import Blueprint

from app.index.controller import(
    ping
)

route = Blueprint('index', __name__)

route.add_url_rule('/ping', view_func=ping, methods=["GET"])

route.add_url_rule(
    "/v1/login",
    view_func=ViewFuncWrapper(
        create_user_view,
        summary="登陆",
        body=CreateUserInSc,
        responses={200: {"schema": BaseModel, "description": "操作成功"}},
        tags=["user"],
    ),
    methods=["POST"],
)

route.add_url_rule(
    "/v1/logout",
    view_func=ViewFuncWrapper(
        create_user_view,
        summary="退出",
        body=CreateUserInSc,
        responses={200: {"schema": BaseModel, "description": "操作成功"}},
        tags=["user"],
    ),
    methods=["POST"],
)