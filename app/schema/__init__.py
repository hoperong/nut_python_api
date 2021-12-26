from typing import Optional
from pydantic import BaseModel, Field


class PageInSc(BaseModel):
    page: Optional[int] = Field(1, description="页数")
    page_size: Optional[int] = Field(10, description="每页数量")


class PageOutSc(BaseModel):
    page: int = Field(description="页数")
    page_size: int = Field(description="每页数量")
    total: int = Field(description="总数")
