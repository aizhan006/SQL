from models import Customer, Tour, Order
from database import session
from datetime import date

# Добавление клиентов
customer_data = [
    {"name": "Иван Иванов", "phone": "1234567890", "email": "ivan@example.com"},
    {"name": "Бакыт Бакытов", "phone": "0987654321", "email": "bakyt@example.com"}
]

for data in customer_data:
    new_customer = Customer(name=data["name"], phone=data["phone"], email=data["email"])
    session.add(new_customer)

session.commit()

# Добавление тура
new_tour = Tour(name="Путешествие в Париж", description="7-дневный тур по Франции",
                price=1200.0, start_date=date(2025, 5, 10), end_date=date(2025, 5, 17))
session.add(new_tour)
session.commit()

# Оформление заказов для клиентов
customers = session.query(Customer).all()
for customer in customers:
    new_order = Order(customer_id=customer.id, tour_id=new_tour.id)
    session.add(new_order)

session.commit()

# Вывод информации о заказах для всех клиентов
for customer in customers:
    for order in customer.orders:
        print(f"Клиент {customer.name} купил тур: {order.tour.name}")
