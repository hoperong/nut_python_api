from pydantic import BaseModel

from flask import Blueprint

from app.user.controller import (
    get_self_view,
    update_self_view,
    get_self_functions_view,
    get_self_menus_view,
    get_users_view,
    get_users_view,
    get_users_view,
    get_users_view,
    get_users_view,
    create_user_view,
    get_user_view,
    update_user_view,
    delete_user_view,
    get_roles_view,
    create_role_view,
    get_role_view,
    update_role_view,
    delete_role_view,
    get_role_function_view,
    update_role_function_view,
    get_functions_view,
    get_menus_view,
    get_role_menu_view,
    update_role_menu_view,
)

from app.user.schema import (
    GetSelfOutSc,
    UpdateSelfInSc,
    GetSelfFunctionsOutSc,
    GetSelfMenusOutSc,
    GetUsersInSc,
    GetUsersOutSc,
    CreateUserInSc,
    GetUserOutSc,
    UpdateUserInSc,
    GetRolesInSc,
    GetRolesOutSc,
    CreateRoleInSc,
    GetRoleOutSc,
    UpdateRoleInSc,
    GetMenusInSc,
    GetMenusOutSc,
    GetRoleMenusOutSc,
    UpdateRoleMenuInSc,
    GetFunctionsInSc,
    GetFunctionsOutSc,
    GetRoleFunctionInSc,
    UpdateRoleFunctionInSc,
    GetMenusInSc,
)

from app.core.api import ViewFuncWrapper

route = Blueprint("user", __name__)

route.add_url_rule(
    "/v1/self",
    view_func=ViewFuncWrapper(
        get_self_view,
        summary="获取自身用户信息",
        responses={200: {"schema": GetSelfOutSc, "description": "获取自身用户信息"}},
        tags=["user"],
    ),
    methods=["GET"],
)

route.add_url_rule(
    "/v1/self",
    view_func=ViewFuncWrapper(
        update_self_view,
        body=UpdateSelfInSc,
        summary="修改自身用户信息",
        responses={200: {"schema": BaseModel, "description": "修改自身用户信息"}},
        tags=["user"],
    ),
    methods=["GET"],
)

route.add_url_rule(
    "/v1/self/functions",
    view_func=ViewFuncWrapper(
        get_self_functions_view,
        summary="获取自身功能权限",
        responses={200: {"schema": GetSelfFunctionsOutSc, "description": "获取自身功能权限"}},
        tags=["user"],
    ),
    methods=["GET"],
)

route.add_url_rule(
    "/v1/self/menus",
    view_func=ViewFuncWrapper(
        get_self_menus_view,
        summary="获取自身菜单权限",
        responses={200: {"schema": GetSelfMenusOutSc, "description": "获取自身菜单权限"}},
        tags=["user"],
    ),
    methods=["GET"],
)

route.add_url_rule(
    "/v1/users",
    view_func=ViewFuncWrapper(
        get_users_view,
        summary="获取用户列表",
        query=GetUsersInSc,
        responses={200: {"schema": GetUsersOutSc, "description": "获取用户列表"}},
        tags=["user"],
    ),
    methods=["GET"],
)
route.add_url_rule(
    "/v1/users",
    view_func=ViewFuncWrapper(
        create_user_view,
        summary="创建用户",
        body=CreateUserInSc,
        responses={200: {"schema": BaseModel, "description": "操作成功"}},
        tags=["user"],
    ),
    methods=["POST"],
)
route.add_url_rule(
    "/v1/users/<user_id>",
    view_func=ViewFuncWrapper(
        get_user_view,
        summary="获取用户详情",
        responses={200: {"schema": GetUserOutSc, "description": "获取用户详情"}},
        tags=["user"],
    ),
    methods=["GET"],
)
route.add_url_rule(
    "/v1/users/<user_id>",
    view_func=ViewFuncWrapper(
        update_user_view,
        summary="修改用户",
        body=UpdateUserInSc,
        responses={200: {"schema": BaseModel, "description": "操作成功"}},
        tags=["user"],
    ),
    methods=["PUT"],
)
route.add_url_rule(
    "/v1/users/<user_id>",
    view_func=ViewFuncWrapper(
        delete_user_view,
        summary="删除用户",
        responses={200: {"schema": BaseModel, "description": "操作成功"}},
        tags=["user"],
    ),
    methods=["DELETE"],
)

route.add_url_rule(
    "/v1/roles",
    view_func=ViewFuncWrapper(
        get_roles_view,
        summary="获取角色列表",
        query=GetRolesInSc,
        responses={200: {"schema": GetRolesOutSc, "description": "获取角色列表"}},
        tags=["role"],
    ),
    methods=["GET"],
)

route.add_url_rule(
    "/v1/roles",
    view_func=ViewFuncWrapper(
        create_role_view,
        summary="创建角色",
        body=CreateRoleInSc,
        responses={200: {"schema": BaseModel, "description": "操作成功"}},
        tags=["role"],
    ),
    methods=["POST"],
)
route.add_url_rule(
    "/v1/roles/<role_id>",
    view_func=ViewFuncWrapper(
        get_role_view,
        summary="获取角色详情",
        responses={200: {"schema": GetRoleOutSc, "description": "获取角色详情"}},
        tags=["role"],
    ),
    methods=["GET"],
)
route.add_url_rule(
    "/v1/roles/<role_id>",
    view_func=ViewFuncWrapper(
        update_role_view,
        summary="修改角色",
        body=UpdateRoleInSc,
        responses={200: {"schema": BaseModel, "description": "操作成功"}},
        tags=["role"],
    ),
    methods=["PUT"],
)
route.add_url_rule(
    "/v1/roles/<role_id>",
    view_func=ViewFuncWrapper(
        delete_role_view,
        summary="删除角色",
        responses={200: {"schema": BaseModel, "description": "操作成功"}},
        tags=["role"],
    ),
    methods=["DELETE"],
)

route.add_url_rule(
    "/v1/menus",
    view_func=ViewFuncWrapper(
        get_menus_view,
        summary="获取菜单权限列表",
        query=GetMenusInSc,
        responses={200: {"schema": GetMenusOutSc, "description": "获取菜单权限列表"}},
        tags=["menu"],
    ),
    methods=["GET"],
)

route.add_url_rule(
    "/v1/roles/<role_id>/menus",
    view_func=ViewFuncWrapper(
        get_role_menu_view,
        summary="获取角色菜单权限列表",
        responses={200: {"schema": GetRoleMenusOutSc, "description": "获取角色菜单权限列表"}},
        tags=["role"],
    ),
    methods=["GET"],
)

route.add_url_rule(
    "/v1/roles/<role_id>/menus",
    view_func=ViewFuncWrapper(
        update_role_menu_view,
        summary="修改角色菜单权限",
        body=UpdateRoleMenuInSc,
        responses={200: {"schema": BaseModel, "description": "操作成功"}},
        tags=["role"],
    ),
    methods=["PUT"],
)

route.add_url_rule(
    "/v1/functions",
    view_func=ViewFuncWrapper(
        get_functions_view,
        summary="获取功能权限列表",
        query=GetFunctionsInSc,
        responses={200: {"schema": GetFunctionsOutSc, "description": "获取功能权限列表"}},
        tags=["function"],
    ),
    methods=["GET"],
)

route.add_url_rule(
    "/v1/roles/<role_id>/functions",
    view_func=ViewFuncWrapper(
        get_role_function_view,
        summary="获取角色功能权限列表",
        responses={200: {"schema": GetRoleFunctionInSc, "description": "获取角色功能权限列表"}},
        tags=["role"],
    ),
    methods=["GET"],
)

route.add_url_rule(
    "/v1/roles/<role_id>/functions",
    view_func=ViewFuncWrapper(
        update_role_function_view,
        summary="修改角色功能权限",
        body=UpdateRoleFunctionInSc,
        responses={200: {"schema": BaseModel, "description": "操作成功"}},
        tags=["role"],
    ),
    methods=["PUT"],
)