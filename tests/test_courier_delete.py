from courier_methods import CouriersMethod
import allure
import requests
import urls
from data import CourierMessages


@allure.sub_suite('class TestDeleteCourier: Удаление курьера')
class TestDeleteCourier:

    @allure.title('Запрос на удаление курьера по существующему id курьера')
    @allure.description(f'Запрос на удаление курьера с существующим id возвращает ' \
                        f'код ответа 200 и тело ответа "{CourierMessages.SUCCESS_DELETE}"')
    def test_success_delete_courier(self, create_courier):
        courier_id = create_courier['courier_id']
        delete_courier_response = CouriersMethod.delete_courier(courier_id)
        assert delete_courier_response.status_code == 200 and delete_courier_response.json() == CourierMessages.SUCCESS_DELETE

    @allure.title('Ошибка при отправке запроса на удаление курьера без id курьера')
    @allure.description(f'Запрос на удаление курьера без id курьера возвращает ' \
                        f'код ответа 400 Bad Request и "message":  "{CourierMessages.NOT_ENOUGH_DATA_DELETE}"')
    def test_bad_request_delete_courier_without_id(self):
        with allure.step('Удаляем курьера без id курьера'):
            delete_courier_response = requests.delete(urls.URL_DELETE_COURIER)
            assert delete_courier_response.status_code == 400 and delete_courier_response.json()['message'] == CourierMessages.NOT_ENOUGH_DATA_DELETE

    @allure.title('Запрос на удаление курьера с несуществующим id курьера')
    @allure.description(f'Запрос на удаление курьера с несуществующим id курьера возвращает ' \
                        f'код ответа 404 Not Found и "message": "{CourierMessages.COURIER_NOT_FOUND}"')
    def test_not_found_delete_courier_with_wrong_id(self):
        with allure.step('Удаляем курьера с несуществующим id курьера'):
            courier_id = '9999999'
            delete_courier_response = CouriersMethod.delete_courier(courier_id)
            assert delete_courier_response.status_code == 404 and delete_courier_response.json()['message']  == CourierMessages.COURIER_NOT_FOUND
