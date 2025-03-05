from sqlalchemy import Column, Integer, String, ForeignKey, Float, Date
from sqlalchemy.orm import relationship
from database import Base, engine


# Таблица клиентов
class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    phone = Column(String, nullable=False, unique=True)
    email = Column(String, nullable=False, unique=True)

    orders = relationship("Order", back_populates="customer")


# Таблица туров
class Tour(Base):
    __tablename__ = 'tours'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    description = Column(String)
    price = Column(Float, nullable=False)
    start_date = Column(Date, nullable=False)
    end_date = Column(Date, nullable=False)

    orders = relationship("Order", back_populates="tour")


# Таблица заказов (Связь между клиентами и турами)
class Order(Base):
    __tablename__ = 'orders'

    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    tour_id = Column(Integer, ForeignKey('tours.id'), nullable=False)

    customer = relationship("Customer", back_populates="orders")
    tour = relationship("Tour", back_populates="orders")


# Создание таблиц в базе данных
Base.metadata.create_all(engine)