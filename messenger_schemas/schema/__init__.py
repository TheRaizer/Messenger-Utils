from contextlib import contextmanager
from typing import Any
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
import logging
from ..environment_variables import (
    RDS_URL,
    RDS_POOL_SIZE,
    RDS_MAX_OVERFLOW,
    RDS_CONNECTION_TIMEOUT,
)

Base: DeclarativeMeta = declarative_base()


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class BaseRecord:
    def key(self) -> Any:
        raise NotImplementedError

    def __eq__(self, other: "BaseRecord"):
        return self.key() == other.key()


def make_engine():
    engine = create_engine(
        RDS_URL,
        pool_size=RDS_POOL_SIZE,
        max_overflow=RDS_MAX_OVERFLOW,
        connect_args={"connect_timeout": RDS_CONNECTION_TIMEOUT},
    )
    return engine


def database_session(engine):
    session: Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()

    try:
        yield session
        if session.dirty:
            session.commit()
    except Exception as e:
        session.rollback()
        logger.error("an error occured while using the database session due to %s", e)
    finally:
        session.close()


def get_db_session_context():
    engine = make_engine()

    def get_database_session():
        return database_session(engine)

    return contextmanager(get_database_session)


DatabaseSession = get_db_session_context()
