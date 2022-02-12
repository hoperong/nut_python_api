# nut_python_api

## 基础规范
+ 每个功能对应一个文件夹，包含
  + controller.py:实现业务逻辑
  + dao.py:实现数据处理逻辑
  + models.py:模型
  + route.py:路由
  + schema.py:接口输入输出验证
+ controller中_view表示url方法
+ route自带自动加载，无需再去向app注册，不过前提是需要使用变量名route定义蓝图，然后把路由都放进route里面
+ route中，使用ViewFuncWrapper处理route对应的func，可以直接生成基于pydantic+openapi的接口文档，地址“/v1/api_doc.html”
## 数据库
开头根据下列含义，对表进行前缀设定
+ TM  主数据表
+ TT  业务数据表
+ TR  关系表
+ TI  接口表
封装了基于alembic的数据库模型管理，使用


## 权限
### 功能权限
Permission对象保存API权限，格式为“Method-URL”，Function对象构成功能权限树，每个节点、叶子节点都对应n条API权限，FunctionPermission保存角色对应的可用功能权限项信息。权限信息一一对应，有父功能权限并没有子功能权限，需要前端一同保存实现。
### 菜单权限
Menu对象构成菜单权限树，RoleMenu保存角色对应的可用菜单项信息。权限信息一一对应，有父菜单权限并没有子菜单权限，需要前端一同保存实现。
### 使用
登录和权限验证是分开的
+ 验证登录：
+ 验证API权限：

## 文字转换

