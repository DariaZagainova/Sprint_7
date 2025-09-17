import requests
import urls
import allure


class CouriersMethod:

    @staticmethod
    @allure.step('Создаём курьера')
    def create_courier(courier_payload):
        response_create = requests.post(urls.URL_CREATE_COURIER, json=courier_payload)
        return response_create

    @staticmethod
    @allure.step('Логинимся курьером')
    def login_courier(courier_payload):
        response_login = requests.post(urls.URL_LOGIN_COURIER, json=courier_payload)
        return response_login

    @staticmethod
    @allure.step('Получаем ID курьера')
    def get_courier_id(response_login):
        if not response_login or response_login.status_code != 200:
            return None
        courier_id = response_login.json().get("id")
        return courier_id

    @staticmethod
    @allure.step('Удаляем курьера')
    def delete_courier(courier_id):
        response_delete = requests.delete(f"{urls.URL_DELETE_COURIER}/{courier_id}")
        return response_delete
