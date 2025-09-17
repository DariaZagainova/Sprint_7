import pytest
from data import DataOrder
import allure
from order_methods import OrderMethods

@allure.sub_suite('class TestCreateOrder: Создание заказа')
class TestOrderCreate:


    @allure.title('Создание заказа с любым выбором цвета самоката')
    @allure.description('Проверяем, что когда создаёшь заказ, можно указать один из цветов — BLACK или GREY, можно указать оба цвета, можно совсем не указывать цвет. ' \
                        'Код ответа 201 Created и тело ответа содержит track ')
    @pytest.mark.parametrize('colors', DataOrder.color_variants)
    def test_create_order_with_colors(self, colors, cancel_order):
        order_data = DataOrder.data_order.copy()
        order_data["color"] = colors
        create_order_response = OrderMethods.create_order(order_data)
        cancel_order["track_number"] = OrderMethods.get_order_track(create_order_response)
        assert create_order_response.status_code == 201 and 'track' in create_order_response.json()
