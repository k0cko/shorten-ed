from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Index

DATABASE_URL = "sqlite:///database.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

metadata = MetaData()

# Define the table structure
urls_table = Table(
    "urls",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("long_url", String, unique=True, nullable=False),
    Column("short_code", String, unique=True, nullable=False),
)

# Index the columns
Index("ix_urls_table_long_short", urls_table.c.long_url, urls_table.c.short_code)

# Create the table in the database
metadata.create_all(engine)