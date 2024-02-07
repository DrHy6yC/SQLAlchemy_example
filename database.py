from os import getenv
from dotenv import load_dotenv

load_dotenv()


class DBMYSQL:
    """Класс который хранит в себе параметры из .env связанные с БД, создает строку подключения к БД

    Attributes
    ----------
    DB_IS_CREATED:
        По этому параметру определяется будет ли созданы/пересозданы таблицы в БД(если True)
    DB_HOST:
        Хост сервера с БД
    DB_PORT:
        Порт подключения к БД
    DB_USER:
        Логин пользователя у которого есть доступ к БД
    DB_PASS:
        пароль учетной записи которой  находится в переменной DB_USER
    DB_NAME:
        Имя бд к которой подключаемся

    Methods
    -------
    get_dsn()
    Необходим для получения строки подключения(dsn)

    get_db_is_created()
    Понадобится что бы перевести строку .env в bool python
    """

    DB_IS_CREATED: bool = getenv('DB_IS_CREATED')
    DB_HOST: str = getenv('DB_HOST')
    DB_PORT: int = getenv('DB_PORT')
    DB_USER: str = getenv('DB_USER')
    DB_PASS: str = getenv('DB_PASS')
    DB_NAME: str = getenv('DB_NAME')

    def get_dsn(self) -> str:
        """
        Метод для получения строки подключения из .env
        :return: строку подключения (str)
        """

        dsn_self = f"mysql+mysqlconnector://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return dsn_self

    def get_db_is_created(self) -> bool:
        """
        Переводит строку из .env в python bool
        :return: Возвращает True когда DB_IS_CREATED=True, в остальных случаях -> False
        """

        if self.DB_IS_CREATED == 'True':
            return True
        else:
            return False
