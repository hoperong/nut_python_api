from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, scoped_session

from app.models.sqlalchemy import Base


class DB:
    def __init__(self, conn=None, echo=True):
        self.conn = conn
        self.engine = None
        self.session = None
        if conn:
            self.engine = create_engine(conn, echo=echo)
            scopefunc = None
            try:
                from greenlet import getcurrent

                scopefunc = getcurrent
            except ImportError:
                from threading import get_ident

                scopefunc = get_ident
            self.session = scoped_session(
                sessionmaker(self.engine), scopefunc=scopefunc
            )

    def get_session(self):
        class NewSession:
            def __init__(self, session):
                self.session = session

            def get_session(self):
                return self.session

        return NewSession(self.session).get_session()

    def get_engine(self):
        class NewEngine:
            def __init__(self, engine):
                self.engine = engine

            def get_engine(self):
                return self.engine

        return NewEngine(self.engine).get_engine()

    def update(self, conn, echo=True):
        self.engine = create_engine(conn, echo=echo)
        scopefunc = None
        try:
            from greenlet import getcurrent

            scopefunc = getcurrent
        except ImportError:
            from threading import get_ident

            scopefunc = get_ident
        options = {}
        options["expire_on_commit"] = False
        options.setdefault("query_cls", Base.query_class)
        self.session = scoped_session(
            sessionmaker(bind=self.engine, **options), scopefunc=scopefunc
        )


db = DB()


def create_db(current_app):
    from app.config.common import config

    conn = config.get("DB_CONNECTION")
    echo = config.get("DB_ECHO")
    db.update(conn, echo)
    from sqlalchemy_utils import database_exists, create_database

    if not database_exists(db.get_engine().url):
        create_database(db.get_engine().url, encoding=config.get("DB_URL_ENCODING"))


def get_session():
    return db.get_session()
