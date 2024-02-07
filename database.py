from os import getenv
from dotenv import load_dotenv

load_dotenv()


class DBMYSQL:
    DB_IS_CREATED: bool = getenv('DB_IS_CREATED')
    DB_HOST: str = getenv('DB_HOST')
    DB_PORT: int = getenv('DB_PORT')
    DB_USER: str = getenv('DB_USER')
    DB_PASS: str = getenv('DB_PASS')
    DB_NAME: str = getenv('DB_NAME')

    def get_dsn(self) -> str:
        dsn_self = f"mysql+mysqlconnector://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"
        return dsn_self

    def get_db_is_created(self) -> bool:
        if self.DB_IS_CREATED == 'True':
            return True
        else:
            return False
