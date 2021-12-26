from typing import List, Optional
from pydantic import BaseModel, Field

from app.schema import PageInSc, PageOutSc
from app.models.pydantic import OrmBase


class GetRolesInSc(PageInSc):
    q: Optional[str] = Field("", description="关键词，支持名称模糊搜索")


class RoleOutSc(OrmBase):
    id: str = Field(description="id")
    name: str = Field(description="名称")
    created_at: float = Field(description="添加时间")
    updated_at: float = Field(description="修改时间")


class GetRolesOutSc(PageOutSc):
    role_list: List[RoleOutSc] = Field(description="角色列表")


class CreateRoleInSc(BaseModel):
    name: str = Field(description="名称")


class GetRoleOutSc(BaseModel):
    role: RoleOutSc = Field(description="角色数据")


class UpdateRoleInSc(BaseModel):
    name: str = Field(description="名称")


class UpdateRoleMenuInSc(BaseModel):
    menu_id_list: List[str] = Field(description="菜单id列表")


class UpdateRoleFunctionInSc(BaseModel):
    function_id_list: List[str] = Field(description="功能id列表")


class GetUsersInSc(PageInSc):
    q: Optional[str] = Field("", description="关键词，支持账号、名称模糊搜索")


class UserOutSc(OrmBase):
    id: str = Field(description="id")
    account: str = Field(description="账号")
    name: str = Field(description="名称")
    is_frozen: bool = Field(description="是否冻结")
    created_at: float = Field(description="添加时间")
    updated_at: float = Field(description="修改时间")
    role_list: List[RoleOutSc] = Field(description="角色列表")


class GetUsersOutSc(PageOutSc):
    user_list: List[UserOutSc] = Field(description="用户列表")


class GetUserOutSc(BaseModel):
    user: UserOutSc = Field(description="用户数据")


class CreateUserInSc(BaseModel):
    account: str = Field(description="账号")
    password: str = Field(description="密码")
    name: str = Field(description="名称")
    role_id_list: List[str] = Field(description="角色id列表")


class UpdateUserInSc(BaseModel):
    name: str = Field(description="名称")
    old_password: str = Field(description="旧密码")
    password: str = Field(description="新密码")
    confirm_password: str = Field(description="确认密码")
    is_frozen: bool = Field(description="是否冻结")
    role_list: List[str] = Field(description="角色列表")


class GetMenusInSc(BaseModel):
    pass


class MenuOutSc(BaseModel):
    id: str = Field(description="id")
    name: str = Field(description="名称")
    desc: str = Field(description="描述")
    key: str = Field(description="唯一代码")
    type: str = Field(description="类型")
    parent_key: str = Field(description="父菜单key")
    created_at: float = Field(description="添加时间")
    updated_at: float = Field(description="修改时间")


class GetMenusOutSc(BaseModel):
    menu_list: List[MenuOutSc] = Field(description="菜单权限列表")


class GetMenuOutSc(BaseModel):
    menu: MenuOutSc = Field(description="菜单权限数据")


class CreateMenuInSc(BaseModel):
    name: str = Field(description="名称")
    desc: str = Field(description="描述")
    key: str = Field(description="唯一代码")
    type: str = Field(description="类型")
    parent_key: str = Field(description="父菜单key")


class UpdateMenuInSc(BaseModel):
    name: str = Field(description="名称")
    desc: str = Field(description="描述")
    key: str = Field(description="唯一代码")
    type: str = Field(description="类型")
    parent_key: str = Field(description="父菜单key")


class GetPermissionsInSc(PageInSc):
    pass


class PermissionOutSc(BaseModel):
    id: str = Field(description="id")
    name: str = Field(description="名称")
    desc: str = Field(description="描述")
    key: str = Field(description="唯一代码")
    parent_key: str = Field(description="父菜单key")
    permission_list: List[str] = Field(description="权限细则列表")
    created_at: float = Field(description="添加时间")
    updated_at: float = Field(description="修改时间")


class GetPermissionsOutSc(PageOutSc):
    permission_list: List[PermissionOutSc] = Field(description="功能权限列表")


class GetPermissionOutSc(BaseModel):
    permission: PermissionOutSc = Field(description="功能权限数据")


class CreatePermissionInSc(BaseModel):
    name: str = Field(description="名称")
    desc: str = Field(description="描述")
    key: str = Field(description="唯一代码")
    parent_key: str = Field(description="父功能key")
    permission_list: List[str] = Field(description="权限细则id列表")


class UpdatePermissionInSc(BaseModel):
    name: str = Field(description="名称")
    desc: str = Field(description="描述")
    key: str = Field(description="唯一代码")
    parent_key: str = Field(description="父功能key")
    permission_list: List[str] = Field(description="权限细则id列表")


class GetFunctionsInSc(BaseModel):
    pass


class FunctionOutSc(BaseModel):
    id: str = Field(description="id")
    name: str = Field(description="名称")
    desc: str = Field(description="描述")
    key: str = Field(description="唯一代码")
    parent_key: str = Field(description="父菜单key")
    permission_list: List[str] = Field(description="权限细则列表")
    created_at: float = Field(description="添加时间")
    updated_at: float = Field(description="修改时间")


class GetFunctionsOutSc(PageOutSc):
    function_list: List[FunctionOutSc] = Field(description="功能权限列表")


class GetFunctionOutSc(BaseModel):
    function: FunctionOutSc = Field(description="功能权限数据")


class CreateFunctionInSc(BaseModel):
    name: str = Field(description="名称")
    desc: str = Field(description="描述")
    key: str = Field(description="唯一代码")
    parent_key: str = Field(description="父功能key")
    permission_list: List[str] = Field(description="权限细则id列表")


class UpdateFunctionInSc(BaseModel):
    name: str = Field(description="名称")
    desc: str = Field(description="描述")
    key: str = Field(description="唯一代码")
    parent_key: str = Field(description="父功能key")
    permission_list: List[str] = Field(description="权限细则id列表")
