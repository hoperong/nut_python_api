import os
import logging

from flask import Flask, g
from werkzeug.exceptions import HTTPException

from app.storage.db import create_db, get_session
from app.core.exception import APIException, InternalServerError, HttpApiException

logger = logging.getLogger()


def auto_load_model():
    """
    仅支持自动加载app目录下的所有文件夹下的models.py文件中的继承了Base对象的模型
    可以配合alembic生成sql更新文件
    """
    result_list = []
    for name in os.listdir("app"):
        if not os.path.isdir(os.path.join("app", name)) or not os.path.exists(
            os.path.join("app", name, "models.py")
        ):
            continue
        model_import = __import__("app.{0}.models".format(name))

        from app.models.sqlalchemy import Base

        for d in dir(model_import.models):
            if d[0] == "_" and d == "Base":
                continue
            m = getattr(model_import.models, d)
            try:
                if isinstance(m(), Base):
                    result_list.append(m)
            except Exception as e:
                logger.debug(e)
    return result_list


def init_db():
    """
    自动创建数据库，更新sql，进行数据填充
    """
    from alembic import command
    from alembic.config import Config
    from app.config.common import config as app_config

    config = Config(app_config.get("ALEMBIC_CONFIG"))
    config.set_main_option("script_location", app_config.get("ALEMBIC_SCRIPT_LOCATION"))
    config.set_main_option("sqlalchemy.url", app_config.get("ALEMBIC_SQLALCHEMY_URL"))
    command.upgrade(config, "head")
    command.stamp(config, "head")


def auto_load_route(app):
    """
    仅支持自动加载app目录下的所有文件夹下的route.py文件中的route对象进app的蓝图里
    """
    for name in os.listdir("app"):
        if not os.path.isdir(os.path.join("app", name)) or not os.path.exists(
            os.path.join("app", name, "route.py")
        ):
            continue
        blueprint = __import__("app.{0}.route".format(name))
        module = getattr(blueprint, name)
        if hasattr(module.route, "route"):
            app.register_blueprint(module.route.route)


def init_i18n(app):
    """
    初始化翻译
    """
    from flask_babel import Babel
    from flask import request
    from app.config.common import config

    app.config["BABEL_TRANSLATION_DIRECTORIES"] = config.get(
        "BABEL_TRANSLATION_DIRECTORIES"
    )
    app.config["BABEL_DEFAULT_LOCALE"] = config.get("BABEL_DEFAULT_LOCALE")
    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        return request.accept_languages.best_match(["en", "zh"])


def init_app(app):
    """
    处理app的生命周期钩子函数
    """

    @app.after_request
    def commit_session(response):
        get_session().commit()
        return response

    @app.teardown_request
    def close_session(response):
        get_session().remove()

    @app.errorhandler(APIException)
    def handler_api_exception(exception):
        return http_error_handler(exception)

    @app.errorhandler(Exception)
    def handler_all_exception(exception):
        return http_error_handler(exception)

    def http_error_handler(exception):
        get_session().remove()
        response = None
        logger.exception(exception)
        if isinstance(exception, APIException):
            response = exception
        elif isinstance(exception, HTTPException):
            response = HttpApiException(exception)
        else:
            response = InternalServerError(str(exception))
        return response.get_response()


def init_auth():
    pass


def init_login(app):
    """
    添加登录插件，手机哟理解那个flask-login，cookie+session来做登录
    todo:后期需要改成jwt+redis来实现高可用
    """
    from flask_login import LoginManager
    from app.config.common import config

    login_manager = LoginManager()
    app.config["SECRET_KEY"] = config.get("SECRET_KEY")
    login_manager.init_app(app)


def create_app():
    app = Flask(__name__)
    # 连接数据库
    create_db(app)
    # 自动加载模型
    auto_load_model()
    init_db()
    # 自动加载权限
    init_auth()
    # 自动加载路由
    auto_load_route(app)
    init_app(app)
    # 添加第三方组件
    init_i18n(app)
    # 添加登录插件
    init_login(app)
    return app
