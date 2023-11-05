from sqlalchemy import Table,Column
from sqlalchemy.sql.sqltypes import Integer,String
from config.db import meta

users = Table(
    'user', meta,
    Column('id',Integer, primary_key=True),
    Column('name',String(50)),
    Column('email',String(20)),
    Column('password',String(20)),
)