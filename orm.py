from icecream import ic
from sqlalchemy import MetaData, Engine
from database import session_sql_connect


def create_all_table(metadata: MetaData, engine: Engine) -> None:
    engine.echo = False
    metadata.drop_all(engine)
    metadata.create_all(engine)
    engine.echo = True


def insert_data_list_to_bd(list_data: list):
    with session_sql_connect() as session_sql:
        ic(list_data)
        session_sql.add_all(list_data)
        session_sql.commit()
