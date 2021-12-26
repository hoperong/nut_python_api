import time

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Boolean, Column
from sqlalchemy.dialects.mysql import DOUBLE
from sqlalchemy.orm.query import Query
from flask_babel import gettext

from app.core.exception import BadRequestException


class _Model:
    """
    Base Model: 包含了 Model 的共有字段和方法
    """

    created_at = Column(
        DOUBLE, nullable=False, default=lambda: time.time(), comment="创建时间"
    )
    updated_at = Column(
        DOUBLE,
        nullable=False,
        default=lambda: time.time(),
        onupdate=lambda: time.time(),
        comment="更新时间",
    )
    deleted_at = Column(
        DOUBLE, nullable=False, default=lambda: time.time(), comment="删除时间"
    )
    deleted = Column(Boolean, default=False, index=True, comment="是否删除")

    def delete(self):
        self.deleted_at = time.time()
        self.deleted = True


class _Query(Query):
    def paginate(self, page=1, page_size=10):
        if page <= 0 or page_size <= 0:
            raise BadRequestException(gettext(u"Invalid query parameter."))
        return self.limit(page_size).offset((page - 1) * page_size)


Base = declarative_base(cls=_Model)
if not getattr(Base, "query_class", None):
    Base.query_class = _Query
