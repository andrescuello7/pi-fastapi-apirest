from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
from config.database import meta, engine


character = Table(
    "characters",
    meta,
    Column("id", Integer, primary_key=True),
    Column("name", String(255)),
    Column("height", Integer),
    Column("mass", Integer),
    Column("hair_color", String(255)),
    Column("skin_color", String(255)),
    Column("eye_color", String(255)),
)

meta.create_all(engine)
