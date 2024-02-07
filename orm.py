from typing import Type

from icecream import ic
from sqlalchemy import Engine, select
from config import session_sql_connect
from models import Base, UsersORM, QuizzesORM


def create_all_table(engine: Engine) -> None:
    """
    Пересоздает(Если есть) все таблицы наследуемые от Base
    :param engine: Принимает sql_engine/подключение
    :return: Ничего не возвращает
    """
    ic(Base.registry.metadata.tables)
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)


def insert_data_list_to_bd(list_data: list) -> None:
    with session_sql_connect() as session_sql:
        session_sql.add_all(list_data)
        session_sql.commit()


def select_from_db(class_orm: Type[UsersORM] | Type[QuizzesORM]) -> list:
    with session_sql_connect() as session_sql:
        query = select(class_orm)
        result_execute = session_sql.execute(query)
        result_select = result_execute.scalars().all()
        ic(result_select)
        return result_select


def update_object(object_orm, new_user_param: str) -> None:
    with session_sql_connect() as session_sql:
        object_orm = session_sql.get(object_orm.__class__, object_orm.ID)
        object_orm.USER_LOGIN = new_user_param
        session_sql.commit()
