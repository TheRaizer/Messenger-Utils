from typing import Any
from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base
import logging
from ..environment_variables import RDS_URL

Base: DeclarativeMeta = declarative_base()


logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

class BaseRecord():
    def key(self) -> Any:
        raise NotImplementedError
    
    def __eq__(self, other: "BaseRecord"):
        return self.key() == other.key()
        

engine = create_engine(RDS_URL)

def database_session():
    session: Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    
    try:
        yield session
        if session.dirty:
            session.commit()
    except Exception as e:
        session.rollback()
        logger.error('an error occured while using the database session due to %s', e)
    finally:
        session.close()
    