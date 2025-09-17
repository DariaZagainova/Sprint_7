from courier_methods import CouriersMethod
import allure
import pytest
from data import CourierMessages


@allure.sub_suite('class TestCourierLogin: Логин курьера')
class TestCourierLogin:

    @allure.title('Курьер может авторизоваться')
    @allure.description('Авторизация курьера с валидными данными (логин и пароль) возвращает ' \
                        'код ответа 200 и в теле ответа есть id курьера')
    def test_sucsses_courier_login(self, create_courier):
        login_courier_response = create_courier['login_courier_response'] 
        assert login_courier_response.status_code == 200 and 'id' in login_courier_response.json()

    @allure.title('Курьер не может авторизоваться c неправильным логином (несуществующий пользователь) или паролем')
    @allure.description(f'Авторизация курерьера с неправильным логином/паролем возвращает ' \
                        f'ошибку 404 Not Found и "message": "{CourierMessages.ACCOUNT_NOT_FOUND}"')
    @pytest.mark.parametrize('error_field', ['login', 'password'])
    def test_courier_cannot_login_with_error_login_or_password(self, create_courier, error_field):
        courier_data_for_login = create_courier['courier_data_for_login'].copy()
        courier_data_for_login[error_field] = '12345'
        login_courier_response = CouriersMethod.login_courier(courier_data_for_login)
        assert login_courier_response.status_code == 404 and login_courier_response.json()["message"] == CourierMessages.ACCOUNT_NOT_FOUND
   
    @allure.title('Курьер не может авторизоваться без поля логина или пароля')
    @allure.description(f'Авторизация курьера без поля логина или пароля возвращает ' \
                        f'ошибку 400 Bad Request и "message": "{CourierMessages.NOT_ENOUGH_DATA_LOGIN}"')
    @pytest.mark.parametrize("missing_field", ["login", "password"])
    def test_courier_cannot_login_without_login_or_password(self, create_courier, missing_field):
        courier_data_for_login = create_courier['courier_data_for_login'].copy()
        courier_data_for_login.pop(missing_field)
        login_courier_response = CouriersMethod.login_courier(courier_data_for_login)
        assert login_courier_response.status_code == 400 and login_courier_response.json()["message"] == CourierMessages.NOT_ENOUGH_DATA_LOGIN
