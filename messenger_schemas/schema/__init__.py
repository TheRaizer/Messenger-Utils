from sqlalchemy.orm import sessionmaker
from sqlalchemy.orm.session import Session
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import DeclarativeMeta, declarative_base

from ..environment_variables import RDS_URL

Base: DeclarativeMeta = declarative_base()

engine = create_engine(RDS_URL)

def database_session():
    session: Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)()
    
    try:
        yield session
        if session.dirty:
            session.commit()
    except:
        session.rollback()
        raise
    finally:
        session.close()
    