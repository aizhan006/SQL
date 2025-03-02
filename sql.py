from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Person(Base):
    tablename = "persons"  # Название таблицы в БД

    id = Column(Integer, primary_key=True)
    name = Column(String)
    age = Column(Integer)

# Пример подключения к БД (SQLite)
engine = create_engine("sqlite:///C:/Users/user/sabak.db")
Base.metadata.create_all(engine)