from icecream import ic

from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker

from database import DBMYSQL


def get_engine(dsn_db) -> Engine:
    engine = create_engine(
        url=dsn_db,
        echo=True
    )
    return engine


db_mysql = DBMYSQL()
dsn = db_mysql.get_dsn()
sql_engine = get_engine(dsn)
session_sql_connect = sessionmaker(sql_engine)
