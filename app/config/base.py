import os

from app.utils.path import get_full_path


class BaseConfig:
    APP_SCHEMA = os.getenv("APP_SCHEMA", "")
    APP_DEBUG = os.getenv("APP_DEBUG", True)

    _DB_CONNECTION = os.getenv(
        "DB_CONNECTION", "mysql+pymysql://root:1234567890@127.0.0.1:3306/nut?charset=utf8mb4")

    # db
    DB_CONNECTION = _DB_CONNECTION

    # alembic
    ALEMBIC_SCRIPT_LOCATION = os.getenv("ALEMBIC_SCRIPT_LOCATION", "migration")
    ALEMBIC_SQLALCHEMY_URL = _DB_CONNECTION
    ALEMBIC_CONFIG = os.getenv(
        "ALEMBIC_CONFIG", get_full_path("static", "config", "alembic.ini"))
