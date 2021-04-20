from pydantic import (BaseModel, Field)


class PageInSc(BaseModel):
    page: int = Field(description="foo value of the request")
    page_size: int = Field(description="foo value of the request")


class PageOutSc(BaseModel):
    page: int = Field(description="foo value of the request")
    page_size: int = Field(description="foo value of the request")
    total: int = Field(description="foo value of the request")

