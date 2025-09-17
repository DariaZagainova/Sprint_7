import allure
import requests
import urls


class OrderMethods:

    @staticmethod
    @allure.step('Создаём заказ')
    def create_order(data_order):
        create_order_response = requests.post(urls.URL_CREATE_ORDERS, json=data_order)
        return create_order_response
    
    @staticmethod
    @allure.step('Получаем track номер созданного заказа')
    def get_order_track(create_order_response):
        track_number = create_order_response.json().get("track")
        return track_number
    
    @staticmethod
    @allure.step('Получаем объект с заказом')
    def get_order_object_by_track(track_number):
        get_order_object_response = requests.get(urls.URL_GET_ORDER_BY_TRACK, params={"t": track_number})
        return get_order_object_response
    
    @staticmethod
    @allure.step('Получаем Id заказа по треку')
    def get_order_id_by_track(track_number):
        get_order_object_response = requests.get(f"{urls.URL_GET_ORDER_BY_TRACK}", params={'t': track_number})
        order_id = get_order_object_response.json().get("order").get("id")
        return order_id
    
    @staticmethod
    @allure.step('Получаем список заказов')
    def get_orders_list():
        orders_list_response = requests.get(urls.URL_GET_ORDERS)
        return orders_list_response
    
    @staticmethod
    @allure.step('Отменяем заказ') 
    def cancel_order(track):
        cancel_order_response = requests.put(urls.URL_CANCEL_ORDER, params={"track": track})
        return cancel_order_response
    
    @staticmethod
    @allure.step('Принимаем заказ')
    def accept_order(order_id, courier_id):
        accept_order_response = requests.put(f"{urls.URL_ACCEPT_ORDER}/{order_id}", params={"courierId": courier_id})
        return accept_order_response

    @staticmethod
    @allure.step('Завершаем заказ') # Только для принятых заказов
    def finish_order(order_id):
        finish_order_response = requests.put(f"{urls.URL_FINISH_ORDER}/{order_id}")
        return finish_order_response
