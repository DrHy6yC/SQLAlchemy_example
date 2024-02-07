from icecream import ic

from config import db_mysql
from config import sql_engine

from models import UsersORM, QuizzesORM
from orm import insert_data_list_to_bd, create_all_table, select_from_db, update_object
from tables_sql import execute_any_query, TRIGGER_USERS_AFTER_UPDATE

if __name__ == "__main__":
    user_di = UsersORM(
        user_tg_id=2312142232,
        user_login='DI_hy6',
        user_full_name='Di Cho Nah'
    )
    grammar_level_test = QuizzesORM(
        quize_name='English Level test. Grammar',
        quize_description='Тест для проверки уровня грамматики по английскому'
    )
    if db_mysql.get_db_is_created():
        create_all_table(sql_engine)
    insert_data_list_to_bd([user_di, grammar_level_test])
    execute_any_query(sql_engine, TRIGGER_USERS_AFTER_UPDATE)
    user_di = select_from_db(UsersORM)[0]
    select_from_db(QuizzesORM)
    update_object(user_di, 'er4r3dewdew')
