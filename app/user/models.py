from uuid import uuid4
from app.models.base import Base
from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship


class User(Base):
    __tablename__ = "TM_user"

    __table_args__ = (
        {"comment": "用户表"}
    )
    id = Column(String(255), primary_key=True,
                default=lambda: str(uuid4()), comment="ID")
    account = Column(String(50), nullable=False, comment="账号", unique=True)
    password = Column(String(255), nullable=False, comment="密码")
    name = Column(String(255), nullable=False, comment="名称")
    # 冻结状态：冻结或者解冻，默认未冻结
    is_frozen = Column(Boolean, nullable=False, default=False, comment="是否冻结")


class Role(Base):
    __tablename__ = "TM_role"

    __table_args__ = (
        {"comment": "角色表"}
    )
    id = Column(String(255), primary_key=True,
                default=lambda: str(uuid4()), comment="ID")
    name = Column(String(255), nullable=False, comment="名称")


class UserRole(Base):
    __tablename__ = "TR_user_role"

    __table_args__ = (
        {"comment": "用户角色表"}
    )
    id = Column(String(255), primary_key=True,
                default=lambda: str(uuid4()), comment="ID")
    user_id = Column(String(255), primary_key=True,
                     default=lambda: str(uuid4()), comment="用户ID")
    user = relationship(
        'User', foreign_keys=[user_id], primaryjoin="UserRole.user_id==User.id", backref="user_role_list")
    role_id = Column(String(255), primary_key=True,
                     default=lambda: str(uuid4()), comment="角色ID")
    role = relationship(
        'Role', foreign_keys=[role_id], primaryjoin="UserRole.role_id==Role.id", backref="user_role_list")


class Resource(Base):
    __tablename__ = "TI_resource"

    __table_args__ = (
        {"comment": "资源表"}
    )
    id = Column(String(255), primary_key=True,
                default=lambda: str(uuid4()), comment="ID")
    name = Column(String(255), nullable=False, comment="名称")
    desc = Column(String(255), nullable=False, comment="描述")
    key = Column(String(255), nullable=False, comment="唯一代码", unique=True)


class Action(Base):
    __tablename__ = "TI_action"

    __table_args__ = (
        {"comment": "操作表"}
    )
    id = Column(String(255), primary_key=True,
                default=lambda: str(uuid4()), comment="ID")
    name = Column(String(255), nullable=False, comment="名称")
    desc = Column(String(255), nullable=False, comment="描述")
    key = Column(String(255), nullable=False, comment="唯一代码", unique=True)


class Permission(Base):
    __tablename__ = "TM_permission"

    __table_args__ = (
        {"comment": "权限细则表"}
    )
    id = Column(String(255), primary_key=True,
                default=lambda: str(uuid4()), comment="ID")
    resource_id = Column(String(255), primary_key=True,
                         default=lambda: str(uuid4()), comment="资源ID")
    resource = relationship('Resource', foreign_keys=[
                            resource_id], primaryjoin="Permission.resource_id==Resource.id", backref="permission_list")
    action_id = Column(String(255), primary_key=True,
                       default=lambda: str(uuid4()), comment="操作ID")
    action = relationship('Action', foreign_keys=[
                          action_id], primaryjoin="Permission.action_id==Action.id", backref="permission_list")


class Module(Base):
    __tablename__ = "TI_module"

    __table_args__ = (
        {"comment": "权限模块表"}
    )
    id = Column(String(255), primary_key=True,
                default=lambda: str(uuid4()), comment="ID")
    name = Column(String(255), nullable=False, comment="名称")
    desc = Column(String(255), nullable=False, comment="描述")
    key = Column(String(255), nullable=False, comment="唯一代码", unique=True)


class Function(Base):
    __tablename__ = "TI_function"

    __table_args__ = (
        {"comment": "权限功能表"}
    )
    id = Column(String(255), primary_key=True,
                default=lambda: str(uuid4()), comment="ID")
    name = Column(String(255), nullable=False, comment="名称")
    desc = Column(String(255), nullable=False, comment="描述")
    key = Column(String(255), nullable=False, comment="唯一代码", unique=True)


class FunctionPermission(Base):
    __tablename__ = "TR_function_permission"

    __table_args__ = (
        {"comment": "权限功能细则表"}
    )
    id = Column(String(255), primary_key=True,
                default=lambda: str(uuid4()), comment="ID")
    function_id = Column(String(255), primary_key=True,
                         default=lambda: str(uuid4()), comment="权限功能ID")
    function = relationship('Function', foreign_keys=[
                            function_id], primaryjoin="FunctionPermission.function_id==Function.id", backref="funciont_permission_list")
    permission_id = Column(String(255), primary_key=True,
                           default=lambda: str(uuid4()), comment="权限细则ID")
    permission = relationship('Permission', foreign_keys=[
                              permission_id], primaryjoin="FunctionPermission.permission_id==Permission.id", backref="funciont_permission_list")


class RoleFunction(Base):
    __tablename__ = "TI_role_function"

    __table_args__ = (
        {"comment": "角色权限功能表"}
    )
    id = Column(String(255), primary_key=True,
                default=lambda: str(uuid4()), comment="ID")
    role_id = Column(String(255), primary_key=True,
                     default=lambda: str(uuid4()), comment="角色ID")
    role = relationship('Role', foreign_keys=[
                        role_id], primaryjoin="RoleFunction.role_id==Role.id", backref="role_function_list")
    function_id = Column(String(255), primary_key=True,
                         default=lambda: str(uuid4()), comment="权限功能ID")
    function = relationship('Function', foreign_keys=[
                            function_id], primaryjoin="RoleFunction.function_id==Function.id", backref="role_function_list")
