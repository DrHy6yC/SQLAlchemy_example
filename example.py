from icecream import ic
from sqlalchemy import create_engine, select, MetaData, insert, Table
from sqlalchemy.engine.base import Engine

from config import dsn
from models import users_table, meta_data

ic(dsn)


def get_engine() -> Engine:
    engine = create_engine(
        url=dsn,
        echo=True
    )
    return engine


def create_table_engine(metadata: MetaData, engine: Engine) -> None:
    engine.echo = False
    metadata.drop_all(engine)
    metadata.create_all(engine)
    engine.echo = True


def select_from_db(engine: Engine, user_table) -> None:
    with engine.connect() as session:
        sql_query = select(user_table)
        res = session.execute(sql_query)
        ic(res.all())


def insert_to_db(engine: Engine, user_table: Table, values_list_dict: list) -> None:
    with engine.connect() as session:
        sql_query = insert(user_table).values(values_list_dict)
        session.execute(sql_query)
        session.commit()


if __name__ == "__main__":
    values = [
        {'USER_TG_ID': 343453, 'USER_FULL_NAME': 'ДИП', 'USER_LOGIN': 'др6с'},
        {'USER_TG_ID': 4345321231, 'USER_FULL_NAME': 'ЛВП', 'USER_LOGIN': 'изипизи'}
    ]
    engine_sql = get_engine()
    create_table_engine(metadata=meta_data, engine=get_engine())
    insert_to_db(engine_sql, users_table, values)
    select_from_db(engine_sql, users_table)
