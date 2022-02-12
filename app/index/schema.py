from typing import List, Optional
from pydantic import BaseModel, Field

from app.schema import PageInSc, PageOutSc
from app.models.pydantic import OrmBase


class LoginUserSc(BaseModel):
    account: str = Field("", description="账号")
    password: str = Field("", description="密码")