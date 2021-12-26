import os


class Config:

    config = None

    def __init__(self):
        if (
            not os.getenv("app_schema")
            or os.getenv("app_schema") == "dev"
            or os.getenv("app_schema") == ""
        ):
            from app.config.dev import DevConfig

            self.config = DevConfig()
        elif os.getenv("app_schema") == "pro":
            from app.config.dev import ProdConfig

            self.config = ProdConfig()
        else:
            from app.config.dev import BaseConfig

            self.config = BaseConfig()

    def get(self, key, default=""):
        if hasattr(self.config, key):
            return getattr(self.config, key)
        else:
            return default if default is not None else ""


config = Config()


def str_to_bool(s):
    pass
