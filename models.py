from sqlalchemy import Table, Column, Integer, BigInteger, String, MetaData
from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase

from database import Base

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


class UsersORM(Base):
    __tablename__ = 'USERS'
    user_tg_id: Mapped[int] = mapped_column(BigInteger)
    user_login: Mapped[str]
    user_full_name: Mapped[str]
    user_level: Mapped[int] = mapped_column(default=0)
    user_access: Mapped[int] = mapped_column(default=0)


class QuizzesORM(Base):
    __tablename__ = 'QUIZZES'
    quize_name: Mapped[str]
    quize_description: Mapped[str]
