from icecream import ic

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

from config import dsn


class Base(DeclarativeBase):
    pass


def get_engine() -> Engine:
    engine = create_engine(
        url=dsn,
        echo=True
    )
    return engine


sql_engine = get_engine()
session_sql_connect = sessionmaker(sql_engine)
