from courier_methods import CouriersMethod
import allure
import requests
import urls


@allure.sub_suite('class TestDeleteCourier: Удаление курьера')
class TestDeleteCourier:

    @allure.title('Запрос на удаление курьера по существующему id курьера')
    @allure.description('Запрос на удаление курьера с существующим id возвращает ' \
                        'код ответа 200 и тело ответа {"ok":true}')
    def test_success_delete_courier(self, create_courier):
        courier_id = create_courier['courier_id']
        delete_courier_response = CouriersMethod.delete_courier(courier_id)
        assert delete_courier_response.status_code == 200 and delete_courier_response.json() == {'ok': True}

    @allure.title('Ошибка при отправке запроса на удаление курьера без id курьера')
    @allure.description('Запрос на удаление курьера без id курьера возвращает ' \
                        'код ответа 400 Bad Request и "message":  "Недостаточно данных для удаления курьера"')
    def test_bad_request_delete_courier_without_id(self):
        with allure.step('Удаляем курьера без id курьера'):
            delete_courier_response = requests.delete(urls.URL_DELETE_COURIER)
            assert delete_courier_response.status_code == 400 and delete_courier_response.json()['message'] == "Недостаточно данных для удаления курьера"

    @allure.title('Запрос на удаление курьера с несуществующим id курьера')
    @allure.description('Запрос на удаление курьера с несуществующим id курьера возвращает ' \
                        'код ответа 404 Not Found и "message": "Курьера с таким id нет."')
    def test_not_found_delete_courier_with_wrong_id(self):
        with allure.step('Удаляем курьера с несуществующим id курьера'):
            courier_id = '9999999'
            delete_courier_response = CouriersMethod.delete_courier(courier_id)
            assert delete_courier_response.status_code == 404 and delete_courier_response.json()['message']  == 'Курьера с таким id нет.'
