import asyncio

from icecream import ic
from sqlalchemy import create_engine, text
from sqlalchemy.ext.asyncio import create_async_engine

from src.config import settings

loop = asyncio.new_event_loop()
asyncio.set_event_loop(loop)


async def tasks():
    await main()


async def main() -> list:
    async_engine = create_async_engine(
        url=settings.DATABASE_URL_asyncpg,
        echo=True
    )
    async with async_engine.connect() as async_conn:
        result_query = await async_conn.execute(text("SELECT VERSION()"))
        ic(result_query.all())

asyncio.run(tasks())
