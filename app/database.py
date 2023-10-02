import time
import psycopg
from psycopg.rows import dict_row
from sqlalchemy import create_engine
from sqlalchemy.ext.asyncio import create_async_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from .config import settings

SQLALCHEMY_DATABASE_URL = f"postgresql+psycopg://{settings.database_username}:{settings.database_password}@{settings.database_hostname}:{settings.database_port}/{settings.database_name}"

engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(engine)

Base = declarative_base()


# class Base(DeclarativeBase):
#     pass


# dependency
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# while True:
#     try:
#         conn = psycopg.connect(
#             host="localhost",
#             dbname="fastAPI",
#             user="postgres",
#             password="password",
#             row_factory=dict_row,
#         )
#         cursor = conn.cursor()
#         print("Database connection was successful!")
#         break
#     except Exception as error:
#         print("Connecting to database failed")
#         print("Error: ", error)
#         time.sleep(2)
