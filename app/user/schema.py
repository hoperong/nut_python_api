from pydantic import Field

from app.schema import (PageInSc, PageOutSc)


class GetUsersInSc(PageInSc):
    q: int = Field("关键词，支持账号、名称模糊搜索")


class GetUsersOutSc(PageOutSc):
    data: int = Field("关键词，支持账号、名称模糊搜索")


class CreateUserInSc(PageInSc):
    account: str = Field("账号")
    password: str = Field("密码")
    name: str = Field("名称")


class CreateUserOutSc(PageInSc):
    q: int = Field("关键词，支持账号、名称模糊搜索")
