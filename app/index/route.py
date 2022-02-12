from flask import Blueprint
from pydantic import BaseModel

from app.index.controller import ping, login, logout
from app.core.api import ViewFuncWrapper
from app.index.schema import LoginUserSc

route = Blueprint("index", __name__)

route.add_url_rule("/ping", view_func=ping, methods=["GET"])

route.add_url_rule(
    "/v1/login",
    view_func=ViewFuncWrapper(
        login,
        summary="登陆",
        body=LoginUserSc,
        responses={200: {"schema": BaseModel, "description": "登录成功"}},
        tags=["index"],
    ),
    methods=["POST"],
)

route.add_url_rule(
    "/v1/logout",
    view_func=ViewFuncWrapper(
        logout,
        summary="退出",
        responses={200: {"schema": BaseModel, "description": "退出成功"}},
        tags=["index"],
    ),
    methods=["POST"],
)