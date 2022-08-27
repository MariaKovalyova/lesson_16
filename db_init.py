import datetime

import data
from db_work import *

db.drop_all()
db.create_all()  # Функция создающая все объекты в БД

"""для заполнения БД.
   Данные берутся из файла data.py
"""
for user in data.USERS:
    db.session.add(User(
        id=user['id'],
        first_name=user['first_name'],
        last_name=user['last_name'],
        age=user['age'],
        email=user['email'],
        role=user['role'],
        phone=user['phone']
    ))
    db.session.commit()  # Записываем данные в ДБ внутри сессии

for order in data.ORDERS:
    month, day, year = [int(i) for i in order['start_date'].split('/')]
    month_end, day_end, year_end = [int(i) for i in order['end_date'].split('/')]
    db.session.add(Order(
        id=order['id'],
        name=order['name'],
        description=order['description'],
        start_date=datetime.date(year=year, month=month, day=day),
        end_date=datetime.date(year=int(year_end), month=int(month_end), day=int(day_end)),
        address=order['address'],
        price=order['price'],
        customer_id=order['customer_id'],
        executor_id=order['executor_id']
    ))
    db.session.commit()

for offer in data.OFFERS:
    db.session.add(Offer(
        id=offer['id'],
        order_id=offer['order_id'],
        executor_id=offer['executor_id']
    ))
    db.session.commit()

db.session.close()  # Закрыть сессию БД
