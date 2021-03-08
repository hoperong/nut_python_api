from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DB:

    session = None

    def __init__(self, conn):
        engine = create_engine(conn)
        self.session = sessionmaker(engine)

    def get_session(self):
        return self.session


db = None


def create_db():
    from app.config.common import config
    conn = config.get("DB_CONNECTION")
    db = DB(conn)


def get_session():
    return db.get_session()
