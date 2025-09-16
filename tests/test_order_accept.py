import requests
from order_methods import OrderMethods
import urls
import allure

@allure.sub_suite('class TestAcceptOrder: Принять заказ')
class TestAcceptOrder:


    @allure.title('Успешный запрос принять заказ')
    @allure.description('Запрос на принятие заказа с существующими id курьера и id заказа возвращает ' \
                        'код ответа 200 и тело ответа {"ok":true}')
    def test_success_accept_order(self, create_order, create_courier):
        order_id = create_order['order_id']
        courier_id = create_courier['courier_id']
        accept_order_response = OrderMethods.accept_order(order_id, courier_id)
        assert accept_order_response.status_code == 200 and accept_order_response.json() == {'ok': True}

    @allure.title('Если не передать id курьера, запрос вернёт ошибку')
    @allure.description('Запрос принять заказ без id курьера возвращает ' \
                        'код ответа 400 Bad Request и "message":  "Недостаточно данных для поиска"')
    def test_do_not_accept_order_without_courier_id(self, create_order):
        order_id = create_order['order_id']
        with allure.step('Отправляем запрос принять заказ без id курьера'):
            accept_order_response = requests.put(f"{urls.URL_ACCEPT_ORDER}/{order_id}")
            assert accept_order_response.status_code == 400 and accept_order_response.json()['message'] == "Недостаточно данных для поиска"
        
    @allure.title('Если передать неверный id курьера, запрос вернёт ошибку')
    @allure.description('Запрос принять заказ с несуществующим id курьера возвращает' \
                        'код ответа 404 Not Found и "message":  "Курьера с таким id не существует"')
    def test_do_not_accept_order_with_nonexistent_courier_id(self, create_order):
        order_id = create_order['order_id']
        courier_id = '9999999'
        with allure.step('Отправляем запрос принять заказ с несуществующим id курьера'):
            accept_order_response = OrderMethods.accept_order(order_id, courier_id)
            assert accept_order_response.status_code == 404 and accept_order_response.json()['message'] == "Курьера с таким id не существует"

    @allure.title('Если не передать id заказа, запрос вернёт ошибку')
    @allure.description('Запрос на принятие заказа без id заказа возвращает ' \
                        'код ответа 400 Bad Request и "message":  "Недостаточно данных для поиска"')    
    def test_do_not_accept_order_without_order_id(self, create_courier):
        courier_id = create_courier['courier_id']
        with allure.step('Отправляем запрос принять заказ без id заказа'):
            accept_order_response = requests.put(urls.URL_ACCEPT_ORDER, params={"courierId": courier_id})
            assert accept_order_response.status_code == 400 and accept_order_response.json()['message'] == "Недостаточно данных для поиска"

    @allure.title('Если передать неверный id заказа, запрос вернёт ошибку')
    @allure.description('Запрос на принятие заказа с несуществующим id заказа возвращает ' \
                        'код ответа 404 Not Found и "message":  "Заказа с таким id не существует"')
    def test_do_not_accept_order_with_nonexistent_order_id(self, create_courier):
        courier_id = create_courier['courier_id']
        order_id = '9999999'
        with allure.step('Отправляем запрос принять заказ с несуществующим id заказа'):
            accept_order = OrderMethods.accept_order(order_id, courier_id)
            assert accept_order.status_code == 404 and accept_order.json()['message'] == "Заказа с таким id не существует"
