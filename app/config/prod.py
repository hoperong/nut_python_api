import os

from app.config.base import BaseConfig


class ProdConfig(BaseConfig):
    APP_SCHEMA = os.getenv("APP_SCHEMA", "prod")
    APP_DEBUG = os.getenv("APP_DEBUG", False)
