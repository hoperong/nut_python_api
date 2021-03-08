import os

from app.config.base import BaseConfig


class DevConfig(BaseConfig):
    APP_SCHEMA = os.getenv("APP_SCHEMA", "dev")
