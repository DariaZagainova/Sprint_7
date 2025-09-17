import requests
from order_methods import OrderMethods
import urls
import allure
from data import OrderMessages, NegativeTestData

@allure.sub_suite('class TestAcceptOrder: Принять заказ')
class TestAcceptOrder:

    @allure.title('Успешный запрос принять заказ')
    @allure.description(f'Запрос на принятие заказа с существующими id курьера и id заказа возвращает ' \
                        f'код ответа 200 и тело ответа "{OrderMessages.SUCCESS_ACCEPT}"')
    def test_success_accept_order(self, create_order, create_courier):
        order_id = create_order['order_id']
        courier_id = create_courier['courier_id']
        accept_order_response = OrderMethods.accept_order(order_id, courier_id)
        assert accept_order_response.status_code == 200 and accept_order_response.json() == OrderMessages.SUCCESS_ACCEPT

    @allure.title('Если не передать id курьера, запрос вернёт ошибку')
    @allure.description(f'Запрос принять заказ без id курьера возвращает ' \
                        f'код ответа 400 Bad Request и "message":  "{OrderMessages.NOT_ENOUGH_DATA_ACCEPT}"')
    def test_do_not_accept_order_without_courier_id(self, create_order):
        order_id = create_order['order_id']
        with allure.step('Отправляем запрос принять заказ без id курьера'):
            accept_order_response = requests.put(f"{urls.URL_ACCEPT_ORDER}/{order_id}")
            assert accept_order_response.status_code == 400 and accept_order_response.json()['message'] == OrderMessages.NOT_ENOUGH_DATA_ACCEPT
        
    @allure.title('Если передать неверный id курьера, запрос вернёт ошибку')
    @allure.description(f'Запрос принять заказ с несуществующим id курьера возвращает' \
                        f'код ответа 404 Not Found и "message":  "{OrderMessages.COURIER_NOT_FOUND_FOR_ACCEPT}"')
    def test_do_not_accept_order_with_nonexistent_courier_id(self, create_order):
        order_id = create_order['order_id']
        courier_id = NegativeTestData.NONEXISTENT_COURIER_ID
        with allure.step('Отправляем запрос принять заказ с несуществующим id курьера'):
            accept_order_response = OrderMethods.accept_order(order_id, courier_id)
            assert accept_order_response.status_code == 404 and accept_order_response.json()['message'] == OrderMessages.COURIER_NOT_FOUND_FOR_ACCEPT

    @allure.title('Если не передать id заказа, запрос вернёт ошибку')
    @allure.description(f'Запрос на принятие заказа без id заказа возвращает ' \
                        f'код ответа 400 Bad Request и "message":  "{OrderMessages.NOT_ENOUGH_DATA_ACCEPT}"')    
    def test_do_not_accept_order_without_order_id(self, create_courier):
        courier_id = create_courier['courier_id']
        with allure.step('Отправляем запрос принять заказ без id заказа'):
            accept_order_response = requests.put(urls.URL_ACCEPT_ORDER, params={"courierId": courier_id})
            assert accept_order_response.status_code == 400 and accept_order_response.json()['message'] == OrderMessages.NOT_ENOUGH_DATA_ACCEPT

    @allure.title('Если передать неверный id заказа, запрос вернёт ошибку')
    @allure.description(f'Запрос на принятие заказа с несуществующим id заказа возвращает ' \
                        f'код ответа 404 Not Found и "message":  "{OrderMessages.ORDER_NOT_FOUND_FOR_ACCEPT}"')
    def test_do_not_accept_order_with_nonexistent_order_id(self, create_courier):
        courier_id = create_courier['courier_id']
        order_id = NegativeTestData.NONEXISTENT_ORDER_ID
        with allure.step('Отправляем запрос принять заказ с несуществующим id заказа'):
            accept_order = OrderMethods.accept_order(order_id, courier_id)
            assert accept_order.status_code == 404 and accept_order.json()['message'] == OrderMessages.ORDER_NOT_FOUND_FOR_ACCEPT
