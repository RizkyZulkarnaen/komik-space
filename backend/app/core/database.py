from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from app.core.config import settings

DATABASE_URL = str(settings.SQLALCHEMY_DATABASE_URL)

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(expire_on_commit=False, autoflush=False, bind=engine)

Base = declarative_base()
