from sqlalchemy import Table, Column, Integer, BigInteger, String, MetaData

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
