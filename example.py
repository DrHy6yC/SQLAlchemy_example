from icecream import ic
from database import get_engine

from models import UsersORM, QuizzesORM
from orm import insert_data_list_to_bd, create_all_table, select_from_db

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
    engine_sql = get_engine()
    create_all_table(UsersORM, engine_sql)
    create_all_table(QuizzesORM, engine_sql)
    insert_data_list_to_bd([user_di, grammar_level_test])
    select_from_db(UsersORM)
    select_from_db(QuizzesORM)
