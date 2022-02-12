from typing import List, Optional
from pydantic import BaseModel, Field

from app.schema import PageInSc, PageOutSc
from app.models.pydantic import OrmBase


class GetSelfOutSc(BaseModel):
    pass


class UpdateSelfInSc(BaseModel):
    pass


class GetSelfFunctionsOutSc(BaseModel):
    pass


class GetSelfMenusOutSc(BaseModel):
    pass


class GetUsersInSc(BaseModel):
    pass


class GetUsersOutSc(BaseModel):
    pass


class CreateUserInSc(BaseModel):
    pass


class GetUserOutSc(BaseModel):
    pass


class UpdateUserInSc(BaseModel):
    pass


class GetRolesInSc(BaseModel):
    pass


class GetRolesOutSc(BaseModel):
    pass


class CreateRoleInSc(BaseModel):
    pass


class GetRoleOutSc(BaseModel):
    pass


class UpdateRoleInSc(BaseModel):
    pass


class GetMenusInSc(BaseModel):
    pass


class GetMenusOutSc(BaseModel):
    pass


class GetRoleMenusOutSc(BaseModel):
    pass


class UpdateRoleMenuInSc(BaseModel):
    pass


class GetFunctionsInSc(BaseModel):
    pass


class GetFunctionsOutSc(BaseModel):
    pass


class GetRoleFunctionInSc(BaseModel):
    pass


class UpdateRoleFunctionInSc(BaseModel):
    pass


class GetMenusInSc(BaseModel):
    pass
