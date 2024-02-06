from sqlalchemy import BigInteger, String
from sqlalchemy.orm import Mapped, mapped_column

from database import Base


class UsersORM(Base):
    __tablename__ = 'USERS'
    id: Mapped[int] = mapped_column(primary_key=True)
    user_tg_id: Mapped[int] = mapped_column(BigInteger)
    user_login: Mapped[str] = mapped_column(String(250))
    user_full_name: Mapped[str] = mapped_column(String(50))
    user_level: Mapped[int] = mapped_column(server_default='0')
    user_access: Mapped[int] = mapped_column(server_default='0')


class QuizzesORM(Base):
    __tablename__ = 'QUIZZES'
    id: Mapped[int] = mapped_column(primary_key=True)
    quize_name: Mapped[str] = mapped_column(String(50))
    quize_description: Mapped[str] = mapped_column(String(250))
