"""Database engine, session factory, and base class for SQLAlchemy models."""

from sqlalchemy.orm.session import Session


from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker

SQLALCHEMY_DATABASE_URL = "sqlite:///./blog.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)


SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


class Base(DeclarativeBase):
    """Declarative base for all ORM models; all models inherit from this."""


def get_db():
    """Dependency that yields a database session; closes after request."""
    with SessionLocal() as db:
        yield db
