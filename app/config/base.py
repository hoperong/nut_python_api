import os


class BaseConfig:
    APP_SCHEMA = os.getenv("APP_SCHEMA", "")

    _DB_CONNECTION = os.getenv(
        "DB_CONNECTION", "mysql+pymysql://root:1234567890@127.0.0.1:3306/nut?charset=utf8mb4")

    # db
    DB_CONNECTION = _DB_CONNECTION

    # alembic
    ALEMBIC_SCRIPT_LOCATION = os.getenv("ALEMBIC_SCRIPT_LOCATION", "migration")
    ALEMBIC_SQLALCHEMY_URL = _DB_CONNECTION
