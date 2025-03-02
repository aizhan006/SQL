from sqlalchemy import create_engine, Column, Integer, String, Date
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import date

# Создаем соединение с базой данных
engine = create_engine("sqlite:///tourism.db")
Base = declarative_base()

# Таблица бронирований (без внешних ключей)
class Booking(Base):
    __tablename__ = 'bookings'

    id = Column(Integer, primary_key=True)
    user = Column(String, nullable=False)  # Имя пользователя
    tour = Column(String, nullable=False)  # Название тура
    price = Column(Integer, nullable=False)  # Цена тура
    booking_date = Column(Date, default=date.today)
    status = Column(String, default="pending")  # "confirmed", "pending", "canceled"

# Создание таблицы
Base.metadata.create_all(engine)

# Создание сессии
Session = sessionmaker(bind=engine)
session = Session()

# --- Добавление тестовых данных ---
if not session.query(Booking).first():
    booking1 = Booking(user="Анна Иванова", tour="Иссык-Куль", price=5000, status="confirmed")
    booking2 = Booking(user="Иван Петров", tour="Ала-Арча", price=3000, status="pending")
    booking3 = Booking(user="Анна Иванова", tour="Ала-Арча", price=3000, status="confirmed")

    session.add_all([booking1, booking2, booking3])
    session.commit()

# --- Вывод всех бронирований ---
results = session.query(Booking).all()

# Вывод заголовков
print("ID | Имя           | Тур         | Цена  | Дата бронирования | Статус")
print("-" * 65)

# Вывод строк бронирования
for row in results:
    print(f"{row.id}  | {row.user:12} | {row.tour:10} | {row.price:5} | {row.booking_date} | {row.status}")

# Закрываем сессию
session.close()
