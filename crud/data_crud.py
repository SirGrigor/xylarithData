from sqlalchemy import Table, Column, Integer, String, JSON

from db.database import metadata, engine

data_table = Table(
    "data",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String),
    Column("region", String),
    Column("additional_info", JSON),
)

metadata.create_all(engine)
