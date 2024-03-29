import os
import logging

from flask import (Flask, g)
from app.storage.db import (create_db, get_session)

logger = logging.getLogger()


def auto_load_model():
    '''
        仅支持自动加载app目录下的所有文件夹下的models.py文件中的继承了Base对象的模型
        可以配合alembic生成sql更新文件
    '''
    result_list = []
    for name in os.listdir('app'):
        if not os.path.isdir(os.path.join('app', name)) or not os.path.exists(os.path.join('app', name, "models.py")):
            continue
        model_import = __import__("app.{0}.models".format(name))

        from app.models.base import Base
        for d in dir(model_import.models):
            if d[0] == '_' and d == "Base":
                continue
            m = getattr(model_import.models, d)
            try:
                if isinstance(m(), Base):
                    result_list.append(m)
            except Exception as e:
                logger.debug(e)
    return result_list


def init_db():
    '''
        自动创建数据库，更新sql，进行数据填充
    '''
    from alembic import command
    from alembic.config import Config
    from app.config.common import config as app_config
    config = Config(app_config.get("ALEMBIC_CONFIG"))
    config.set_main_option(
        "script_location", app_config.get("ALEMBIC_SCRIPT_LOCATION"))
    config.set_main_option(
        "sqlalchemy.url", app_config.get("ALEMBIC_SQLALCHEMY_URL"))
    command.upgrade(config, "head")
    command.stamp(config, "head")


def auto_load_route(app):
    '''
        仅支持自动加载app目录下的所有文件夹下的route.py文件中的route对象进app的蓝图里
    '''
    for name in os.listdir('app'):
        if not os.path.isdir(os.path.join('app', name)) or not os.path.exists(os.path.join('app', name, "route.py")):
            continue
        blueprint = __import__("app.{0}.route".format(name))
        module = getattr(blueprint, name)
        if hasattr(module.route, "route"):
            app.register_blueprint(module.route.route)


def init_i18n(app):
    '''
        初始化翻译
    '''
    from flask_babel import Babel
    from flask import request
    from app.config.common import config
    app.config["BABEL_TRANSLATION_DIRECTORIES"] = config.get(
        "BABEL_TRANSLATION_DIRECTORIES")
    app.config["BABEL_DEFAULT_LOCALE"] = config.get("BABEL_DEFAULT_LOCALE")
    babel = Babel(app)

    @babel.localeselector
    def get_locale():
        # return request.accept_languages.best_match(['en', 'zh'])
        return 'zh'


def init_app(app):
    '''
        处理app的生命周期钩子函数
    '''
    @app.after_request
    def commit_session(response):
        get_session().commit()
        return response

    @app.teardown_request
    def close_session(response):
        get_session().remove()


def create_app():
    app = Flask(__name__)
    # 连接数据库
    create_db(app)
    # 自动加载模型
    auto_load_model()
    init_db()
    # 自动加载路由
    auto_load_route(app)
    init_app(app)
    # 添加第三方组件
    init_i18n(app)
    return app
