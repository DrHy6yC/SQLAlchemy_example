from icecream import ic
from sqlalchemy import create_engine, text
from sqlalchemy.engine.base import Engine

from config import URL

url = URL()
dsn = url.get_dsn()
ic(dsn)


def get_engine() -> Engine:
    engine = create_engine(
        url=dsn,
        echo=True
    )
    return engine


def select_from_db(query: str) -> None:
    with get_engine().connect() as session:
        res = session.execute(text(query))
        ic(res.all())


if __name__ == "__main__":
    select_from_db("SELECT VERSION()")
