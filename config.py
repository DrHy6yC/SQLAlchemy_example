from sqlalchemy import create_engine
from sqlalchemy.engine.base import Engine
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncEngine
from sqlalchemy.orm import sessionmaker

from database import DBMYSQL


def get_engine(dsn_db: str) -> Engine:
    """
    Функция запуска главного движка sql/подключения синхронно
    :param dsn_db: Принимает в себя строку подключения
    :return: возвращает экземпляр класса Engine из sqlalchemy.engine.base
    """
    engine = create_engine(
        url=dsn_db,
        echo=True
    )
    return engine


def get_async_engine(async_dsn_db: str) -> AsyncEngine:
    """
    Функция запуска главного движка sql/подключения асинхронно
    :param async_dsn_db: Принимает в себя строку асинхронного подключения
    :return: возвращает aсинхронный экземпляр класса Engine из sqlalchemy.engine.base
    """
    engine = create_async_engine(
        url=async_dsn_db,
        echo=True
    )
    return engine


db_mysql = DBMYSQL()
# sync
dsn = db_mysql.get_lite_dsn()#db_mysql.get_dsn()
sql_engine = get_engine(dsn)
session_sql_connect = sessionmaker(sql_engine)

# async
async_dsn = db_mysql.get_async_dsn()
sql_async_engine = get_async_engine(async_dsn)
async_session_sql_connect = async_sessionmaker(sql_async_engine)
