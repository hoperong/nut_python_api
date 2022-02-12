import os

from app.utils.path import get_full_path
from app.utils.utils import (
    str2bool,
    str2int,
)


class BaseConfig:
    APP_SCHEMA = os.getenv("APP_SCHEMA", "")
    APP_DEBUG = str2bool(os.getenv("APP_DEBUG"), True)
    APP_HOST = os.getenv("APP_HOST", "0.0.0.0")
    APP_PORT = str2int(os.getenv("APP_PORT"), 8000)

    SECRET_KEY = os.getenv("SECRET_KEY","6e355fce-15bc-4892-be47-2b4e8c8dd64e")

    _DB_CONNECTION = os.getenv(
        "DB_CONNECTION",
        "mysql+pymysql://root:1234567890@127.0.0.1:3306/nut?charset=utf8mb4",
    )

    # db
    DB_CONNECTION = _DB_CONNECTION
    DB_URL_ENCODING = os.getenv("DB_URL_ENCODING", "utf8mb4")
    DB_ECHO = str2bool(os.getenv("DB_ECHO"), True)

    # alembic
    ALEMBIC_SCRIPT_LOCATION = os.getenv("ALEMBIC_SCRIPT_LOCATION", "migration")
    ALEMBIC_SQLALCHEMY_URL = _DB_CONNECTION
    ALEMBIC_CONFIG = os.getenv(
        "ALEMBIC_CONFIG", get_full_path("static", "config", "alembic.ini")
    )

    # BABEL
    BABEL_TRANSLATION_DIRECTORIES = os.getenv(
        "BABEL_TRANSLATION_DIRECTORIES", get_full_path("static", "i18n")
    )
    BABEL_DEFAULT_LOCALE = os.getenv("BABEL_DEFAULT_LOCALE", "zh")

    # api_doc
    API_DOC_TEMPLATES = os.getenv(
        "API_DOC_TEMPLATES", get_full_path("static", "templates", "api_doc")
    )
