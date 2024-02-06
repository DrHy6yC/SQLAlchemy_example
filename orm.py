from icecream import ic
from sqlalchemy import Engine, select
from database import session_sql_connect, Base


def create_all_table(base: Base, engine: Engine) -> None:
    engine.echo = False
    base.metadata.drop_all(engine)
    base.metadata.create_all(engine)
    engine.echo = True


def insert_data_list_to_bd(list_data: list):
    with session_sql_connect() as session_sql:
        session_sql.add_all(list_data)
        session_sql.commit()


def select_from_db(class_orm: Base) -> None:
    with session_sql_connect() as session_sql:
        query = select(class_orm)
        result_execute = session_sql.execute(query)
        result_select = result_execute.scalars().all()
        ic(result_select)
