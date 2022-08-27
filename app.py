from flask import Flask, jsonify, request

from utils import *  # Импорт функций для работы с запросами

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mybase.db'  # Адрес БД
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False

db = SQLAlchemy(app)


@app.route("/users", methods=['GET', 'POST'])
@app.route("/offers", methods=['GET', 'POST'])
@app.route("/orders", methods=['GET', 'POST'])
def all_page():
    route_str = request.base_url.split('/')[-1][:-1].capitalize()  # Получение названия словаря
    if request.method == 'GET':
        result = []
        for obj in globals()[route_str].query.all():  # str название словаря превращаем в перменную
            result.append((obj.to_dict()))
        return jsonify(result)
    if request.method == 'POST':
        print(route_str)
        add_obj(route_str)  # Вызов фунции добавления данных из db_work.py
        return "Информация добавлена", 200


@app.route('/users/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/offers/<int:id>', methods=['GET', 'PUT', 'DELETE'])
@app.route('/orders/<int:id>', methods=['GET', 'PUT', 'DELETE'])
def find_by_user_id(id):
    route_str = request.base_url.split('/')[-2][:-1].capitalize()  # Получаем название словаря, которое потом будет переменной
    if request.method == 'GET':
        obj = globals()[route_str].query.get(id)  # Делаем из названия словаря одноимённую переменную
        return jsonify(obj.to_dict())
    elif request.method == 'PUT':
        obj_put(route_str, id)  # Вызов функции добавления из папки utils.py
        return f'Объект с id {id} успешно изменён!', 200

    elif request.method == 'DELETE':
        obj_delete(route_str, id)  # Вызов функции удаления из папки utils.py
        return f"Объект с id {id} успешно удалён!", 200


if __name__ == "__main__":
    """ 127.0.0.1:5000 - дефолтный IP-адрес """
    app.run(debug=True)
