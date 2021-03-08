import os

from flask import Flask

from app.storage.db import create_db


def auto_load_model():
    '''
        仅支持自动加载app目录下的所有文件夹下的route.py文件中的route对象进app的蓝图里
        如果还有其他需求请自行在下面加
    '''
    result_list = []
    for name in os.listdir('app'):
        if not os.path.isdir(os.path.join('app', name)) or not os.path.exists(os.path.join('app', name, "models.py")):
            continue
        model_import = __import__("app.{0}.models".format(name))
        print(dir(model_import))

        from app.models.base import Base
        for d in dir(model_import.models):
            if d[0] == '_' and d == "Base":
                continue
            m = getattr(model_import.models, d)
            try:
                if isinstance(m(), Base):
                    result_list.append(m)
            except Exception as e:
                print(e)
    print(result_list)
    return result_list


def init_db():
    '''
    '''


def auto_load_route(app):
    '''
        仅支持自动加载app目录下的所有文件夹下的route.py文件中的route对象进app的蓝图里
    '''
    for name in os.listdir():
        if not os.path.isdir(name) or not os.path.exists(os.path.join(name, "route.py")):
            continue
        blueprint = __import__("{0}.route".format(name))
        if hasattr(blueprint.route, "route"):
            app.register_blueprint(blueprint.route.route)


def create_app():
    app = Flask(__name__)
    # 连接数据库
    create_db()
    # 自动加载模型
    auto_load_model()
    # init_db()
    # 自动加载路由
    auto_load_route(app)
    return app


if __name__ == "__main__":
    flask_app = create_app()
    flask_app.run()
