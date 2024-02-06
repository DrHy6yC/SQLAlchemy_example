from icecream import ic

from sqlalchemy import MetaData, Table, Column, Integer, BigInteger, String, select, insert
from sqlalchemy.engine.base import Engine
# Альтернатива orm


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


def create_all_table(metadata: MetaData, engine: Engine) -> None:
    engine.echo = False
    metadata.drop_all(engine)
    metadata.create_all(engine)
    engine.echo = True


meta_data = MetaData()

users_table = Table(
    "USERS",
    meta_data,
    Column("ID", Integer, primary_key=True),
    Column("USER_TG_ID", BigInteger),
    Column("USER_FULL_NAME", String(250)),
    Column("USER_LEVEL", Integer, default=0),
    Column("USER_ACCESS", Integer, default=0),
    Column("USER_LOGIN", String(50))
)


quizzes_table = Table(
    "QUIZZES",
    meta_data,
    Column("ID", Integer, primary_key=True),
    Column("QUIZE_NAME", String(250)),
    Column("QUIZE_DESCRIPTION", String(500))
)
