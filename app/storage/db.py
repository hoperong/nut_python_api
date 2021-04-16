from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DB:

    session = None
    engine = None

    def __init__(self, conn):
        self.engine = create_engine(conn)
        self.session = sessionmaker(self.engine)

    def get_session(self):
        return self.session

    def get_engine(self):
        return self.engine


db = None


def create_db():
    from app.config.common import config
    conn = config.get("DB_CONNECTION")
    db = DB(conn)
    from sqlalchemy_utils import database_exists, create_database
    if not database_exists(db.get_engine().url):
        create_database(db.get_engine().url)


def get_session():
    return db.get_session()
