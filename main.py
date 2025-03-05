from models import Customer, Tour, Order
from database import session
from datetime import date

# Добавление клиента
new_customer = Customer(name="Иван Иванов", phone="1234567890", email="ivan@example.com")
session.add(new_customer)
session.commit()

# Добавление тура
new_tour = Tour(name="Путешествие в Париж", description="7-дневный тур по Франции",
                price=1200.0, start_date=date(2025, 5, 10), end_date=date(2025, 5, 17))
session.add(new_tour)
session.commit()

# Оформление заказа
new_order = Order(customer_id=new_customer.id, tour_id=new_tour.id)
session.add(new_order)
session.commit()

# Вывод информации о заказе
customer = session.query(Customer).filter_by(name="Иван Иванов").first()
for order in customer.orders:
    print(f"Клиент {customer.name} купил тур: {order.tour.name}")
