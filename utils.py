import json  # Json
import datetime  # Импорт работы со временем

from flask import Flask, request  # Импорт Flask и запросов
from flask_sqlalchemy import SQLAlchemy  # Импорт для работы с SQL

from db_work import *  # Импортируем классы БД из файла db_work.py

app = Flask(__name__)  # Подключение к приложению
db = SQLAlchemy(app)  # Подключение к ДБ

''' Функции для работы с запросами'''

"""Функция добавления объекта в БД"""
def add_obj(data_name):
    obj = json.loads(request.data)  # Получаем данные из запроса
    if data_name == "User":
        new_data = User(
            id=obj['id'],
            first_name=obj['first_name'],
            last_name=obj['last_name'],
            age=obj['age'],
            email=obj['email'],
            role=obj['role'],
            phone=obj['phone']
        )
    elif data_name == "Offer":
        new_data = Offer(
            id=obj['id'],
            order_id=obj['order_id'],
            executor_id=obj['executor_id']
        )
    elif data_name == "Order":
        month, day, year =[int(o) for o in obj['start_date'].split("/")]
        month_end, day_end, year_end = obj['end_date'].split('/')
        new_data = Order(
            id=obj['id'],
            name=obj['name'],
            description=obj['description'],
            start_date=datetime.date(year=year, month=month, day=day),
            end_date=datetime.date(year=int(year_end), month=int(month_end), day=int(day_end)),
            address=obj['address'],
            price=obj['price'],
            customer_id=obj['customer_id'],
            executor_id=obj['executor_id']
        )
    db.session.add(new_data)
    db.session.commit()


def obj_put(data_name, id):  # Заропрос PUT
    user_data = json.loads(request.data)
    obj = db.session.query(globals()[data_name]).get(id)
    if data_name == "User":
        obj.first_name = user_data['first_name']
        obj.last_name = user_data['last_name']
        obj.phone = user_data['phone']
        obj.role = user_data['role']
        obj.email = user_data['email']
        obj.age = user_data['age']
    elif data_name == "Offer":
        obj.order_id == user_data['order_id']
        obj.executor_id == user_data['executor_id']
    elif data_name == "Order":
        month, day, year = [int(o) for o in user_data['start_date'].split("/")]
        month_end, day_end, year_end = user_data['end_date'].split('/')
        obj.name == user_data['name']
        obj.description == user_data['description']
        obj.start_date == datetime.date(year=year, month=month, day=day),
        obj.end_date == datetime.date(year=int(year_end), month=int(month_end), day=int(day_end))
        obj.address == user_data['address']
        obj.price == user_data['price']
        obj.customer_id == user_data['customer_id']
        obj.executor_id == user_data['executor_id']
    db.session.add(obj)
    db.session.commit()


def obj_delete(data_name, id):  # Запрос DELETE
    obj = db.session.query(globals()[data_name]).get(id)
    db.session.delete(obj)
    db.session.commit()
