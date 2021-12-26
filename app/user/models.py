from uuid import uuid4
from app.models.sqlalchemy import Base
from sqlalchemy import Boolean, Column, String, ForeignKey
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "TM_user"

    __table_args__ = {"comment": "用户表"}
    id = Column(
        String(255), primary_key=True, default=lambda: str(uuid4()), comment="ID"
    )
    account = Column(String(50), nullable=False, comment="账号", unique=True)
    password = Column(String(255), nullable=False, comment="密码")
    name = Column(String(255), nullable=False, comment="名称")
    is_admin = Column(Boolean, nullable=False, default=False, comment="是否属于管理，是的话不可删除")
    # 冻结状态：冻结或者解冻，默认未冻结
    is_frozen = Column(Boolean, nullable=False, default=False, comment="是否冻结")


class Role(Base):
    __tablename__ = "TM_role"

    __table_args__ = {"comment": "角色表"}
    id = Column(
        String(255), primary_key=True, default=lambda: str(uuid4()), comment="ID"
    )
    name = Column(String(255), nullable=False, comment="名称")
    is_admin = Column(Boolean, nullable=False, default=False, comment="是否属于管理，是的话不可删除")


class UserRole(Base):
    __tablename__ = "TR_user_role"

    __table_args__ = {"comment": "用户角色表"}
    id = Column(
        String(255), primary_key=True, default=lambda: str(uuid4()), comment="ID"
    )
    user_id = Column(
        String(255),
        default=lambda: str(uuid4()),
        comment="用户ID",
    )
    user = relationship(
        "User",
        foreign_keys=[user_id],
        primaryjoin="UserRole.user_id==User.id",
        backref="user_role_list",
    )
    role_id = Column(
        String(255),
        default=lambda: str(uuid4()),
        comment="角色ID",
    )
    role = relationship(
        "Role",
        foreign_keys=[role_id],
        primaryjoin="UserRole.role_id==Role.id",
        backref="user_role_list",
    )


class Permission(Base):
    __tablename__ = "TI_permission"

    __table_args__ = {"comment": "权限细则表"}
    id = Column(
        String(255), primary_key=True, default=lambda: str(uuid4()), comment="ID"
    )
    url = Column(String(255), nullable=False, comment="url", unique=True)


class Function(Base):
    __tablename__ = "TI_function"

    __table_args__ = {"comment": "权限功能表"}
    id = Column(
        String(255), primary_key=True, default=lambda: str(uuid4()), comment="ID"
    )
    name = Column(String(255), nullable=False, comment="名称")
    desc = Column(String(255), nullable=False, comment="描述")
    key = Column(String(255), nullable=False, comment="唯一代码", unique=True)
    parent_key = Column(String(255), nullable=False, comment="父功能key")


class FunctionPermission(Base):
    __tablename__ = "TR_function_permission"

    __table_args__ = {"comment": "权限功能细则表"}
    id = Column(
        String(255), primary_key=True, default=lambda: str(uuid4()), comment="ID"
    )
    function_id = Column(String(255), default=lambda: str(uuid4()), comment="权限功能ID")
    function = relationship(
        "Function",
        foreign_keys=[function_id],
        primaryjoin="FunctionPermission.function_id==Function.id",
        backref="funciont_permission_list",
    )
    permission_id = Column(String(255), default=lambda: str(uuid4()), comment="权限细则ID")
    permission = relationship(
        "Permission",
        foreign_keys=[permission_id],
        primaryjoin="FunctionPermission.permission_id==Permission.id",
        backref="funciont_permission_list",
    )


class RoleFunction(Base):
    __tablename__ = "TR_role_function"

    __table_args__ = {"comment": "角色权限功能表"}
    id = Column(
        String(255), primary_key=True, default=lambda: str(uuid4()), comment="ID"
    )
    role_id = Column(String(255), default=lambda: str(uuid4()), comment="角色ID")
    role = relationship(
        "Role",
        foreign_keys=[role_id],
        primaryjoin="RoleFunction.role_id==Role.id",
        backref="role_function_list",
    )
    function_id = Column(String(255), default=lambda: str(uuid4()), comment="权限功能ID")
    function = relationship(
        "Function",
        foreign_keys=[function_id],
        primaryjoin="RoleFunction.function_id==Function.id",
        backref="role_function_list",
    )


class Menu(Base):
    __tablename__ = "TI_menu"

    __table_args__ = {"comment": "权限菜单表"}
    id = Column(
        String(255), primary_key=True, default=lambda: str(uuid4()), comment="ID"
    )
    name = Column(String(255), nullable=False, comment="名称")
    desc = Column(String(255), nullable=False, comment="描述")
    key = Column(String(255), nullable=False, comment="唯一代码", unique=True)
    type = Column(String(255), nullable=False, comment="类型")
    parent_key = Column(String(255), nullable=False, comment="父菜单key")


class RoleMenu(Base):
    __tablename__ = "TR_role_menu"

    __table_args__ = {"comment": "角色权限菜单表"}
    id = Column(
        String(255), primary_key=True, default=lambda: str(uuid4()), comment="ID"
    )
    role_id = Column(String(255), default=lambda: str(uuid4()), comment="角色ID")
    role = relationship(
        "Role",
        foreign_keys=[role_id],
        primaryjoin="RoleFunction.role_id==Role.id",
        backref="role_menu_list",
    )
    menu_id = Column(String(255), default=lambda: str(uuid4()), comment="菜单权限ID")
    menu = relationship(
        "Menu",
        foreign_keys=[menu_id],
        primaryjoin="RoleMenu.menu_id==Menu.id",
    )
