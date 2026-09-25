# config.py
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    DATABASE_URL: str = os.getenv('DATABASE_URL', 'sqlite:///./test.db')
    SECRET_KEY: str = os.getenv('SECRET_KEY', 'supersecret')
    ALGORITHM: str = 'HS256'
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30

settings = Settings()

# database.py
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(settings.DATABASE_URL, connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# get_db dependency
from contextlib import contextmanager

@contextmanager
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
