from sqlalchemy.orm import declarative_base ,sessionmaker
from sqlalchemy import create_engine

engine=create_engine("postgresql://postgres:pgadmin123@localhost/users",echo=True)
Base =declarative_base()

SessionLocal=sessionmaker(bind=engine)