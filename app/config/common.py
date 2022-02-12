import os


class Config:

    config = None

    def __init__(self):
        if (
            not os.getenv("APP_SCHEMA")
            or os.getenv("APP_SCHEMA") == "dev"
            or os.getenv("APP_SCHEMA") == ""
        ):
            from app.config.dev import DevConfig

            self.config = DevConfig()
        elif os.getenv("APP_SCHEMA") == "pro":
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