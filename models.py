import datetime
from typing import Annotated

from sqlalchemy import BigInteger, String, func
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

int_pk = Annotated[int, mapped_column(primary_key=True)]
big_int = Annotated[int, mapped_column(BigInteger)]
int_serv_def_0 = Annotated[int, mapped_column(server_default='0')]

date_now = Annotated[datetime.datetime, mapped_column(server_default=func.now())]

str_256 = Annotated[str, mapped_column(String(256))]
str_50 = Annotated[str, mapped_column(String(50))]


class Base(DeclarativeBase):
    pass


class UsersORM(Base):
    __tablename__ = 'USERS'
    id: Mapped[int_pk]
    user_tg_id: Mapped[big_int]
    user_login: Mapped[str_256]
    user_full_name: Mapped[str_256]
    user_level: Mapped[int_serv_def_0]
    user_access: Mapped[int_serv_def_0]
    user_create_time: Mapped[date_now]
    user_edit_time: Mapped[date_now]


class QuizzesORM(Base):
    __tablename__ = 'QUIZZES'
    id: Mapped[int_pk]
    quize_name: Mapped[str_50]
    quize_description: Mapped[str_256]


class UserQuizzesORM(Base):
    __tablename__ = 'USER_QUIZZES'
    id: Mapped[int_pk]
