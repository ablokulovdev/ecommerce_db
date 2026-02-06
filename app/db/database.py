from sqlalchemy import create_engine,URL
from sqlalchemy.orm import declarative_base,sessionmaker
from app.settings.config import DBNAME,USER,PASS,PORT,HOST


DATABASE_URL = URL.create(
    "postgresql+psycopg2",
    username=USER,
    password=PASS,
    host=HOST,
    port=PORT,
    database=DBNAME
)

engin = create_engine(DATABASE_URL)

SessionLocal = sessionmaker(bind=engin)

Base = declarative_base()

