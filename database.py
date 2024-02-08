from os import getenv
from dotenv import load_dotenv

load_dotenv()


class DBMYSQL:
    """Класс который хранит в себе параметры из .env связанные с БД, создает строку подключения к БД

    Attributes
    ----------
    DB_IS_CREATED : bool
        По этому параметру определяется будет ли созданы/пересозданы таблицы в БД(если True)
    DB_HOST : str
        Хост сервера с БД
    DB_PORT : int
        Порт подключения к БД
    DB_USER : str
        Логин пользователя у которого есть доступ к БД
    DB_PASS : str
        пароль учетной записи которой  находится в переменной DB_USER
    DB_NAME : str
        Имя бд к которой подключаемся
    DB_lite_SQL : str
        Путь и имя файла к БД SQL lite (name_db.db)

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
    DB_lite_SQL: str = getenv('DB_lite_SQL')

    def get_lite_dsn(self) -> str:
        """Метод для получения строки подключения для lite SQL
        :return: строку подключения (str)
        """

        dsn_self = f"sqlite+pysqlite:///{self.DB_lite_SQL}"
        return dsn_self

    def get_lite_async_dsn(self) -> str:
        """Метод для получения строки подключения для lite SQL асинхронно
        :return: строку подключения (str)
        """

        dsn_self = f"sqlite+aiosqlite:///{self.DB_lite_SQL}"
        return dsn_self

    def get_dsn(self) -> str:
        """Метод для получения строки подключения из .env
        :return: строку подключения (str)
        """

        dsn_self = f"mysql+mysqlconnector://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return dsn_self

    def get_async_dsn(self) -> str:
        """Метод для получения строки подключения из .env
        :return: строку асинхронного подключения (str)
        """
        dsn_self = f"mysql+aiomysql://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
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
