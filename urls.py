BASE_URL = "https://qa-scooter.praktikum-services.ru"

# Курьер
URL_CREATE_COURIER = f"{BASE_URL}/api/v1/courier" # Создание курьера
URL_LOGIN_COURIER = f"{BASE_URL}/api/v1/courier/login" # Логин курьера в системе
URL_DELETE_COURIER = f"{BASE_URL}/api/v1/courier" # Удаление курьера + /:id

# Заказ
URL_CREATE_ORDERS = f"{BASE_URL}/api/v1/orders" # Создание заказа и получение списка заказов
URL_GET_ORDERS = f"{BASE_URL}/api/v1/orders" # Получение списка заказов
URL_CANCEL_ORDER = f"{BASE_URL}/api/v1/orders/cancel" # Отмена заказа
URL_ACCEPT_ORDER = f"{BASE_URL}/api/v1/orders/accept" # Принять заказ
URL_GET_ORDER_BY_TRACK = f"{BASE_URL}/api/v1/orders/track" # Получить заказ по его номеру
URL_FINISH_ORDER = f"{BASE_URL}/api/v1/orders/finish"# Завершить заказ