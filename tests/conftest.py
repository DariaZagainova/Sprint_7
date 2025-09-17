import pytest
from generators import generate_courier_payload
from courier_methods import CouriersMethod
from order_methods import OrderMethods
from data import DataOrder


# Данные для создания курьера; удаление курьера
@pytest.fixture
def courier_payload():
    courier_data = generate_courier_payload()   
    yield courier_data
    courier_data_for_login = courier_data.copy()
    courier_data_for_login.pop("firstName", None)
    login_courier_response = CouriersMethod.login_courier(courier_data_for_login)
    courier_id = CouriersMethod.get_courier_id(login_courier_response)
    CouriersMethod.delete_courier(courier_id)

# Данные для авторизации курьера, авторизация курьера, id курьера; удаление курьера
@pytest.fixture
def create_courier():
    courier_data = generate_courier_payload()
    CouriersMethod.create_courier(courier_data)
    courier_data_for_login = courier_data.copy()
    courier_data_for_login.pop("firstName", None)
    login_courier_response = CouriersMethod.login_courier(courier_data_for_login)
    courier_id = CouriersMethod.get_courier_id(login_courier_response)
    yield {
        'courier_data': courier_data,
        "courier_data_for_login": courier_data_for_login,
        "login_courier_response": login_courier_response,
        "courier_id": courier_id
    }
    CouriersMethod.delete_courier(courier_id)

# Создает заказ, трек номер заказа, id заказа; отменяет созданный заказ, удаляет принятый заказ
@pytest.fixture
def create_order():
    create_order_response = OrderMethods.create_order(DataOrder.data_order)
    track_number = OrderMethods.get_order_track(create_order_response)
    order_id = OrderMethods.get_order_id_by_track(track_number)
    yield { 
        'track_number': track_number,
        'order_id': order_id
    }
    OrderMethods.cancel_order(track_number)
    OrderMethods.finish_order(order_id )

# Отмена созданного заказа
@pytest.fixture
def cancel_order():
    track_number = {"track_number": None}
    yield track_number
    OrderMethods.cancel_order(track_number["track_number"])
