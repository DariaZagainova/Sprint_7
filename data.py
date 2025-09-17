
# Данные для заказа
class DataOrder:

    data_order = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": 4,
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": []
    }

    # Варианты цветов самоката
    color_variants = [
        ["BLACK"],         # только черный
        ["GREY"],          # только серый
        ["BLACK", "GREY"], # оба цвета
        []                 # без выбора цвета
    ]

# Сообщения ответов

# Для курьера
class CourierMessages:

    # Успешные ответы
    SUCCESS_CREATION = {"ok": True}
    SUCCESS_DELETE = {"ok": True}

    # Ошибки
    LOGIN_ALREADY_USED = "Этот логин уже используется"
    NOT_ENOUGH_DATA_CREATE = "Недостаточно данных для создания учетной записи"
    ACCOUNT_NOT_FOUND = "Учетная запись не найдена"
    NOT_ENOUGH_DATA_LOGIN = "Недостаточно данных для входа"
    NOT_ENOUGH_DATA_DELETE = "Недостаточно данных для удаления курьера"
    COURIER_NOT_FOUND = "Курьера с таким id нет"

#Для заказа
class OrderMessages:

    # Успешные ответы
    SUCCESS_ACCEPT = {"ok": True}

    # Ошибки
    NOT_ENOUGH_DATA_GET_ORDER = "Недостаточно данных для поиска" # Получить данные заказа
    ORDER_NOT_FOUND = "Заказ не найден"
    NOT_ENOUGH_DATA_ACCEPT = "Недостаточно данных для поиска" # Принять данные заказа
    COURIER_NOT_FOUND_FOR_ACCEPT = "Курьера с таким id не существует"
    ORDER_NOT_FOUND_FOR_ACCEPT = "Заказа с таким id не существует"

# Данные для негативных сценариев
class NegativeTestData:
    NONEXISTENT_ORDER_ID = '9999999' #несуществующий id заказа
    NONEXISTENT_COURIER_ID = '9999999' #несуществующий id курьера
    NONEXISTENT_TRACK_NUMBER = '9999999' #несуществующий трек номер заказа
    
