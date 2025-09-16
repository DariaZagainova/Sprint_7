from order_methods import OrderMethods
import allure
import requests
import urls


@allure.sub_suite('class TestGetOrderList: Список заказов')
class TestGetOrderList:

    @allure.title('Успешный запрос возвращает список заказов')
    @allure.description('Проверяем, что запрос списка заказов возвращает ' \
                        'код ответа 200 и тело ответа возвращает список заказов')
    def test_get_orders_returns_list(self):
        list_order_response = OrderMethods.get_orders_list()
        assert list_order_response.status_code == 200 and 'orders' in list_order_response.json() and type(list_order_response.json()['orders']) is list

@allure.sub_suite('class TestGetOrderByNumber: Получить заказ по его трек номеру')
class TestGetOrderByNumber:

    @allure.title('Успешный запрос возвращает объект с заказом')
    @allure.description('Запрос получения заказа с существующими трэк номером возвращает ' \
                        'код ответа 200 и объект с заказом')
    def test_success_get_order_by_track(self, create_order):
        track_number = create_order['track_number']
        get_order = OrderMethods.get_order_object_by_track(track_number)
        assert get_order.status_code == 200 and 'order' in get_order.json() 

    @allure.title('Запрос без номера заказа возвращает ошибку')
    @allure.description('Запрос получения заказа без трэк номера возвращает ' \
                        'код ответа 400 Bad Request и "message":  "Недостаточно данных для поиска"')
    def test_error_get_order_without_track_number(self):
        with allure.step('Отправляем запрос без трэк номера заказа'):
            get_order_response = requests.get(urls.URL_GET_ORDER_BY_TRACK)
            assert get_order_response.status_code == 400 and get_order_response.json()["message"] == "Недостаточно данных для поиска"

    @allure.title('Запрос с несуществующим заказом возвращает ошибку')
    @allure.description('Запрос получения заказа с несуществующим трэк номером заказа возвращает ' \
                        'код ответа 404 Not Found и "message":  "Заказ не найден"')
    def test_error_get_order_with_nonexistent_number(self):
        with allure.step('Отправляем запрос c несуществующим номером заказом'):
            track_number = '9999999'
            get_order = OrderMethods.get_order_object_by_track(track_number)
            assert get_order.status_code == 404 and get_order.json()["message"] == "Заказ не найден"
