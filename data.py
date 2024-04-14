class ApiEndpoints:
    BASE_URL = 'https://qa-scooter.praktikum-services.ru'
    CREATE_COURIER = BASE_URL + '/api/v1/courier'
    LOGIN = BASE_URL + '/api/v1/courier/login'
    ORDER = BASE_URL + '/api/v1/orders'

class AnswersCreateCourier:
    create_courier_success = '{"ok":true}'
    error_message_create_courier_fail = "Этот логин уже используется. Попробуйте другой."
    error_message_without_login = 'Недостаточно данных для создания учетной записи'
    error_message_without_password = 'Недостаточно данных для создания учетной записи'

class AnswersLoginCourier:
    login_courier_success = 'id'
    error_message_incorrect_password = 'Учетная запись не найдена'
    error_message_non_existent_user = 'Учетная запись не найдена'
    error_message_courier_missing_one_attribute = 'Недостаточно данных для входа'