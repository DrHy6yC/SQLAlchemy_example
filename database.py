from icecream import ic

from sqlalchemy import create_engine, select, insert, Table
from sqlalchemy.engine.base import Engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, mapped_column, Mapped

from config import dsn


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


def get_engine() -> Engine:
    engine = create_engine(
        url=dsn,
        echo=True
    )
    return engine


sql_engine = get_engine()
session_sql_connect = sessionmaker(sql_engine)


def select_from_db(engine: Engine, name_table) -> None:
    with engine.connect() as session:
        sql_query = select(name_table)
        res = session.execute(sql_query)
        ic(res.all())


def insert_to_db(engine: Engine, user_table: Table, values_list_dict: list) -> None:
    with engine.connect() as session:
        sql_query = insert(user_table).values(values_list_dict)
        session.execute(sql_query)
        session.commit()
