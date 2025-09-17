import allure
import pytest
from courier_methods import CouriersMethod
from data import CourierMessages


@allure.sub_suite('class TestCourierCreate: Создание курьера')
class TestCourierCreate:

    @allure.title('Курьера можно создать')
    @allure.description(f'Запрос на создание курьера с заполненными валидными данными в полях login, password, firstName возвращает ' \
                        f'код ответа 201 Created и тело ответа "{CourierMessages.SUCCESS_CREATION}"')
    def test_success_create_courier(self, courier_payload):
        courier_data = courier_payload
        create_courier_response = CouriersMethod.create_courier(courier_data)
        assert create_courier_response.status_code == 201 and create_courier_response.json() == CourierMessages.SUCCESS_CREATION

    @allure.title("Курьера можно создать без имени")
    @allure.description(f'Запрос на созданиие курьера с заполненными валидными данными в полях login, password и без поля firstName возвращает ' \
                        f'код ответа 201 Created и тело ответа "{CourierMessages.SUCCESS_CREATION}"')
    def test_can_create_courier_without_name(self, courier_payload):
        courier_data = courier_payload.copy()
        courier_data.pop('firstName', None)
        create_courier_response = CouriersMethod.create_courier(courier_data)
        assert create_courier_response.status_code == 201 and create_courier_response.json() == CourierMessages.SUCCESS_CREATION

    @allure.title('Нельзя создать двух одинаковых курьеров')
    @allure.description(f'Попытка создания курьера с уже занятым логином должна вернуть ' \
                        f'ошибку 409 Conflict и "message": "{CourierMessages.LOGIN_ALREADY_USED}"')
    def test_duplicate_courier_creation_fail(self, create_courier):
        courier_data = create_courier['courier_data']
        create_courier_again = CouriersMethod.create_courier(courier_data)
        assert create_courier_again.status_code == 409 and create_courier_again.json()["message"] == CourierMessages.LOGIN_ALREADY_USED

    @allure.title("Нельзя создать курьера без логина или пароля")
    @allure.description(f'Если одного из полей нет, запрос возвращает ' \
                        f'ошибку 400 Bad Request и "message": "{CourierMessages.NOT_ENOUGH_DATA_CREATE}"')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_cannot_create_courier_without_login_or_password(self, courier_payload, missing_field):
        courier_data = courier_payload.copy()
        courier_data.pop(missing_field)
        create_courier_response = CouriersMethod.create_courier(courier_data)
        assert create_courier_response.status_code == 400 and create_courier_response.json()["message"] == CourierMessages.NOT_ENOUGH_DATA_CREATE
