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
)

Base: DeclarativeMeta = declarative_base()

"""
    When you run session.close() it releases all the resources it might have used, i.e. transactional/connection. 
    It does not physically close the session so that no other queries can be run after you have called it.
    
    "The close() method issues a expunge_all(), and releases any transactional/connection resources. 
    When connections are returned to the connection pool, transactional state is rolled back as well."
    
    So it would still run the query after you called session.close(). Any uncommitted transactions, as stated above, will be rolled back.
    
    Because of the fact that the connection is returned to the pool without actually closing the connection with the database,
    after a certain amount of time, a request to the database will cause a "MySQL server has gone away" error.
    
    To avoid this we set pool_pre_ping to true. This sends a test ping before any actual
    database requests to the database to test a possibly stale connection.
    This test ping will recover the possibly stale connection, avoiding the 
    "MySQL server has gone away" error.
    
    reference: https://docs.sqlalchemy.org/en/14/core/pooling.html#disconnect-handling-pessimistic
"""
engine = create_engine(
    RDS_URL,
    pool_size=RDS_POOL_SIZE,
    max_overflow=RDS_MAX_OVERFLOW,
    pool_pre_ping=True,
)

logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)


class BaseRecord:
    def key(self) -> Any:
        raise NotImplementedError

    def __eq__(self, other: "BaseRecord"):
        return self.key() == other.key()


def database_session():
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
