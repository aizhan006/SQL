from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Подключение к SQLite
engine = create_engine('sqlite:///tourist.db', echo=True)

# Создание базового класса
Base = declarative_base()

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()