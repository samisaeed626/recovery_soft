from app.config import settings
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


engine = create_engine(settings.db_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    """
    This function yield db instance, which can be imported from here into other
    modules and apps. Rather than returning the instance immediately, we're using
    the "yield" keyword so that it doesn't get loaded into RAM as soon as it's created
    """
    db = SessionLocal()
    try:
        yield db
    except:
        db.close()
